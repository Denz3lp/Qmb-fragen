from flask import Flask, render_template, request, redirect, url_for, session
import csv
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def load_questions():
    questions = []
    with open('questions.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            question = row[0]
            options = row[1].split(';')
            correct_answer = row[2].strip()
            questions.append((question, options, correct_answer))
    random.shuffle(questions)
    return questions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    session['questions'] = load_questions()
    session['current_question'] = 0
    session['score'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        current_question = session['current_question']
        questions = session['questions']
        
        if selected_answer == questions[current_question][2]:
            session['score'] += 1

        session['current_question'] += 1

        if session['current_question'] >= len(questions):
            return redirect(url_for('result'))

    current_question = session['current_question']
    question_data = session['questions'][current_question]
    question_text = question_data[0]
    options = question_data[1]

    return render_template('quiz.html', question=question_text, options=options)

@app.route('/result')
def result():
    score = session['score']
    total_questions = len(session['questions'])
    percentage = (score / total_questions) * 100
    passed = percentage >= 60
    return render_template('result.html', score=score, total=total_questions, percentage=percentage, passed=passed)

if __name__
