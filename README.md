🕵️‍♀️ Fake Review Detection System

A full-stack AI-powered web app that detects fake or overly subjective product reviews using sentiment analysis.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-orange)
![Deployed](https://img.shields.io/badge/Status-Deployed-green)

📌 Features

- 🔍 Detects **fake vs genuine** reviews using TextBlob NLP
- 📋 Admin Dashboard to view & delete flagged reviews
- 📊 Pie chart visualization of review status (Chart.js)
- 📤 Upload multiple reviews using CSV
- 🗑️ Delete individual reviews with one click
- 🌐 Deploy-ready on Render

## 🧠 How It Works

The system uses:
- Polarity: Measures how positive/negative the review is
- Subjectivity: Measures how opinion-based the review is

If a review is very subjective and very positive, it is flagged as “Fake/Suspicious”.

python
if subjectivity > 0.75 and polarity > 0.6:
    return "Fake/Suspicious"
🚀 Live Demo
🌍 Try the Live App on Render
🔗 View Code on GitHub

💻 Tech Stack
Python + Flask

HTML5, CSS3, Bootstrap

TextBlob (NLP)

SQLite (local DB)

Chart.js (for pie chart)

📂 Project Setup
bash
Copy code
git clone https://github.com/PRAGATHIVAISHNAVI11/fake-review-detector.git
cd fake-review-detector
pip install -r requirements.txt
python app.py
Then open http://127.0.0.1:5000 in your browser.

📷 Screenshots
🧾 Review Submission

📊 Dashboard

🙋‍♀️ Created by
👩‍💻 Pragathi Vaishnavi
3rd Year Computer Science Student
