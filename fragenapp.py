import tkinter as tk
from tkinter import messagebox
import random
import csv

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.question = []
        self.current_question = 0
        self.score = 0

        self.load_question()

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.show_question()

    def load_questions(self):
        with open('question.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                question = row[0]
                options = row[1].split(';')
                correct_answer = row[2]
                self.questions.append((question, options, correct_answer))
        random.shuffle(self.questions)

    def show_question(self):
        if self.current_question < len(self.questions):
            question, options, _ = self.questions[self.current_question]
            self.question_label.config(text=f"Q: {question}\nOptions: {', '.join(options)}")
            self.answer_var.set("")
            self.result_label.config(text="")
        else:
            self.end_quiz()

    def check_answer(self):
        _, _, correct_answer = self.questions[self.current_question]
        if self.answer_var.get().strip() == correct_answer.strip():
            self.result_label.config(text="Correct!")
            self.score += 1
        else:
            self.result_label.config(text=f"Wrong! Correct answer was: {correct_answer}")
        self.submit_button.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.submit_button.config(state=tk.NORMAL)
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        result_text = f"Quiz Over! Your score: {self.score}/{total_questions} ({percentage:.2f}%)"
        if percentage >= 60:
            result_text += "\nYou Passed!"
        else:
            result_text += "\nYou Failed!"
        messagebox.showinfo("Quiz Result", result_text)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
