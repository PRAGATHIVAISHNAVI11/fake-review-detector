from flask import Flask, render_template, request, redirect
import sqlite3
from textblob import TextBlob
import csv
from io import TextIOWrapper

app = Flask(__name__)

def analyze_review(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if subjectivity > 0.75 and polarity > 0.6:
        return "Fake/Suspicious"
    else:
        return "Genuine"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    review = request.form['review']
    status = analyze_review(review)
    conn = sqlite3.connect("reviews.db")
    conn.execute("CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, status TEXT)")
    conn.execute("INSERT INTO reviews (content, status) VALUES (?, ?)", (review, status))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM reviews WHERE status='Genuine'")
    genuine_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM reviews WHERE status='Fake/Suspicious'")
    fake_count = cursor.fetchone()[0]
    conn.close()
    return render_template("dashboard.html", reviews=rows, genuine_count=genuine_count, fake_count=fake_count)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect("reviews.db")
    conn.execute("DELETE FROM reviews WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "Empty file", 400
    stream = TextIOWrapper(file.stream, encoding='utf-8')
    reader = csv.reader(stream)
    conn = sqlite3.connect("reviews.db")
    for row in reader:
        if row:
            review = row[0]
            status = analyze_review(review)
            conn.execute("INSERT INTO reviews (content, status) VALUES (?, ?)", (review, status))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)