# AI Resume Critiquer 📃🤖

An AI-powered web application that analyzes resumes and provides structured, actionable feedback using Google's Gemini AI.

---

## 🚀 Features

* 📄 Upload resumes in PDF or TXT format
* 🤖 AI-powered resume analysis
* 🎯 Role-specific feedback based on target job role
* 📊 Structured suggestions for improvement
* ⚡ Fast and interactive UI with Streamlit

---

## 🧠 How It Works

1. User uploads a resume
2. Text is extracted using PyPDF2
3. Resume content is sent to Gemini AI
4. AI analyzes:

   * Content clarity
   * Skills presentation
   * Experience descriptions
   * Job-role alignment
5. Structured feedback is displayed

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **AI Model**: Google Gemini API
* **Libraries**:

  * PyPDF2
  * python-dotenv
  * google-generativeai / google-genai

---

## 📂 Project Structure

ai-resume-critiquer/
│
├── app.py (main Streamlit app)
├── debug_models.py (for debugging models)
├── requirements.txt
├── README.md
├── .env (not included in repo)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/ai-resume-critiquer.git
cd ai-resume-critiquer

---

### 2️⃣ Create Virtual Environment

python -m venv .venv
.venv\Scripts\activate   (Windows)

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Add Environment Variables

Create a `.env` file in root folder:

GEMINI_API_KEY=your_api_key_here

---

### 5️⃣ Run Application

streamlit run app.py

---

## 🔐 Environment Variables

| Variable       | Description                |
| -------------- | -------------------------- |
| GEMINI_API_KEY | Your Google Gemini API Key |

---

## ⚠️ Important Notes

* Ensure your API key supports text generation models
* Do NOT upload `.env` file to GitHub
* Recommended model: gemini-1.5-flash / gemini-2.5-flash

---

## 🚀 Future Improvements

* 📊 Resume scoring system (ATS score)
* 🔍 Keyword optimization
* 🌐 Deploy on cloud (Streamlit / Render)
* 📥 Downloadable feedback report

---

## 👨‍💻 Author

Adarsh M
BTech CSE (AI/ML)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
