from flask import Flask, render_template, request, session, redirect, url_for
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = InferenceClient(
    provider="together",
    api_key=HF_TOKEN
)

def get_course_recommendations(user_input, history):
    try:
        context = ""
        for turn in history:
            context += f"User: {turn['user']}\nBot: {turn['bot']}\n"
        prompt = f'''
        You are a helpful and smart course advisor bot. You give 2-3 real, specific online courses from sites like Coursera, Udemy, edX, NPTEL or LinkedIn Learning. You do not give fake courses or Google search links. You only recommend courses that are real and available online.

        Each course should include:
        1. Course Title – Platform
        🔗 Direct clickable link to course
        Brief description of the course (max 1-2 sentences)
        NEVER give fake placeholders or Google search links.
        Don't add any blank lines between the course title, the link and brief description of the course.
        After each course, add a line with "--------------------------------------------------------" to separate courses.

        Only recommend which course to start with for a specific year (first, second, third, final) if the user directly asks. Do not give unsolicited advice about which course is best for a particular year unless asked. Do not give unsolicited advice about which course to start with if you have experience or interested in certification unless the user asks.

        If the user asks a follow-up (like "which one is better for me if I'm in 2nd or any specific year") or which course to start with or best if interested in certification, use the previously suggested course titles in your answer.
        {context}
        User: {user_input}
        Bot: '''
        completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print("Error in get_course_recommendations:", e)
        return "Sorry, an error occurred."

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_course_recommendations(user_input, session["chat_history"])
        session["chat_history"].append({"user": user_input, "bot": bot_response})
    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/clear", methods=["POST"])
def clear():
    session.pop("chat_history", None)
    return redirect(url_for("index"))

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == "__main__":
    app.run()