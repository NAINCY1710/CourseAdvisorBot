# 🎓 Smart Course Advisor Bot

A personalized web app that recommends real, high-quality online courses tailored to your interests and academic year powered by advanced AI and live course search.

---

## 🚀 Features

- 🤖 Get 2-3 real up-to-date course recommendations from Coursera, Udemy, edX, NPTEL and LinkedIn Learning
- 🧑‍🎓 Ask for suggestions specific to your year (first, second, third, final) or area of interest
- 📝 Each course includes a title, platform, direct link and a concise description
- 💬 Chat interface with conversation history and easy clearing
- 🌐 Minimalistic responsive UI for a seamless experience

---

## 🧠 Powered By

- **Mistral Mixtral 8x7B** for smart context-aware recommendations
- **Flask** for backend and session management
- **Jinja2** for dynamic HTML rendering

---

## 💻 Setup

```bash
git clone https://github.com/NAINCY1710/CourseAdvisorBot.git
cd CourseAdvisorBot
python -m venv venv
venv\Scripts\activate         # for Windows
source venv/bin/activate      # for Linux/macOS
pip install -r requirements.txt
python api/app.py
```

---

## 🔐 Configuration
Before running the app, add your Hugging Face token and Flask secret key to a `.env file` in the project root
```bash
HF_TOKEN = "your_huggingface_token"
SECRET_KEY = "your_flask_secret_key"
```

---

## 👨‍💻 Contributors

- [Naincy Jain](https://www.linkedin.com/in/naincy-jain-38a20a283)
- [Aarjav Jain](https://www.linkedin.com/in/bharatwalejain)