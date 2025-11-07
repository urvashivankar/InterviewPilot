# 🎯 InterviewPilot — AI Interview Agent

An AI-powered mock interview system that asks role-specific technical questions, evaluates answers, and generates follow-up questions — just like a real interviewer.

🚀 Built using **Streamlit + Google Gemini API**

---

## 🌟 Demo (Local Setup)

| Component | Link |
|----------|------|
| ✅ GitHub Repo | https://github.com/urvashivankar/InterviewPilot |
| ✅ Tech Stack | Streamlit + Python + Gemini API |

---

## 🔥 Features

✅ Simulates real interview experience  
✅ Role-based interview (Machine Learning, Data Analyst, Backend, etc.)  
✅ Adaptive follow-up questions  
✅ Gives short feedback/evaluation before next question  
✅ Sleek Streamlit UI  
✅ Gemini-powered — fast response & reasoning

---

## 🧠 How it works

1. User enters a job role (e.g., "Machine Learning Engineer")
2. App triggers Gemini API to start an interview conversation
3. User types answers in chat
4. AI evaluates and asks follow-up questions

Pseudo flow:

```text
User gives role → AI starts interview → User answers → AI evaluates + continues

🛠 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/urvashivankar/InterviewPilot.git
cd InterviewPilot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add Gemini API Key

Create a new file:

.streamlit/secrets.toml


Paste this:

GEMINI_KEY = "YOUR_API_KEY_HERE"

4️⃣ Run the app
streamlit run app.py

🧩 Project Structure
InterviewPilot/
│── app.py                # Streamlit UI
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
└── .streamlit/
    └── secrets.toml      # API key (ignored by Git)

⚙️ Tech Stack
Layer	Technology
Frontend UI	Streamlit
Backend Logic	Python
LLM	Google Gemini (gemini-flash-latest, gemini-2.5-flash)
Deployment	Streamlit Cloud / HuggingFace (optional)
✨ Future Enhancements

✅ Export interview transcript

✅ Add scoring system

✅ Resume-based interview mode (upload CV → get interview questions)

💡 Usage Scenarios

Preparing for ML/Data Science interviews

Practicing system design / problem solving

Mock interview practice for college placements

❤️ Contribution

Contributions are welcome!

To contribute:

git checkout -b feature-name
git commit -m "added new feature"
git push origin feature-name

⭐ Show Support

If you like this project, please ⭐ star the repository.
It motivates me to build more awesome projects!

👉 https://github.com/urvashivankar/InterviewPilot

Made with ❤️ by Urvashi Vankar
