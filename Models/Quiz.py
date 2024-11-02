import dotenv
import os
from .Teacher import Teacher
from .Question import Question
import mysql.connector as msc
import csv
from datetime import datetime
from .Question import Question

class Quiz:
    def __init__(self, made_by, assigned_to_batch, assigned_to_semester, no_of_questions, total_marks, questions, last_date, number_of_attempts, quiz_id, name):
        self.made_by = made_by
        self.assigned_to_batch = assigned_to_batch
        self.assigned_to_semester = assigned_to_semester
        self.no_of_questions = no_of_questions
        self.last_date = last_date
        self.number_of_attempts = number_of_attempts
        self.quiz_id = quiz_id
        self.name = name 
        self.questions = self.load_questions()
        self.total_marks = self.calculate_total_marks()
    def load_questions(self):
        SQL_PASSWORD = os.getenv("SQL_PASSWORD")
        conn = msc.connect(host='localhost', user='root', password=SQL_PASSWORD, database='quiz_system')
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM question WHERE quiz_id = {self.quiz_id}")
        question_ids = cursor.fetchall()
        questions = []
        for question_id in question_ids:
            question = Question.from_sql(question_id[0])
            questions.append(question)
        cursor.close()
        conn.close()
        return questions
    def calculate_total_marks(self):
        total_marks = 0
        for question in self.questions:
            total_marks += question.marks
        return total_marks
    def attempts_left(self, student_id):
        SQL_PASSWORD = os.getenv("SQL_PASSWORD")
        conn = msc.connect(host='localhost', user='root', password=SQL_PASSWORD, database='quiz_system')
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM attempt WHERE student_roll_no = '{student_id}' AND quiz_id = {self.quiz_id}")
        attempts = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return self.number_of_attempts - attempts
    @staticmethod
    def get_quizzes(batch,semester):
        SQL_PASSWORD = os.getenv("SQL_PASSWORD")
        conn = msc.connect(host='localhost', user='root', password=SQL_PASSWORD, database='quiz_system')
        cursor = conn.cursor()

        # Load quiz ids for the specified batch and semester
        cursor.execute(f"""
            SELECT id
            FROM quiz
            WHERE batch_id = '{batch}' AND semester = '{semester}'
        """)
        quiz_ids = cursor.fetchall()

        quizzes = []
        for quiz_id in quiz_ids:
            quiz = Quiz.from_sql(quiz_id[0])
            if quiz:
                quizzes.append(quiz)
        cursor.close()
        conn.close()

        return quizzes

    @staticmethod
    def from_sql(quiz_id):
        SQL_PASSWORD = os.getenv("SQL_PASSWORD")
        conn = msc.connect(host='localhost', user='root', password=SQL_PASSWORD, database='quiz_system')
        cursor = conn.cursor(dictionary=True)

        # Load quiz and teacher data using join
        cursor.execute(f"""
            SELECT q.*, t.name as teacher_name, t.username as teacher_username, t.password as teacher_password
            FROM quiz q
            JOIN teacher t ON q.teacher_id = t.id
            WHERE q.id = {quiz_id}
        """)
        quiz_data = cursor.fetchone()
        if not quiz_data:
            return None

        made_by = quiz_data['teacher_name']
        assigned_to_batch = quiz_data['batch_id']
        assigned_to_semester = quiz_data['semester']
        no_of_questions = int(quiz_data['no_of_questions'])
        total_marks = None  # This will be calculated
        questions = []  # This should be loaded from another source
        last_date = datetime.strptime(quiz_data['last_date'], '%Y-%m-%d')
        number_of_attempts = int(quiz_data['attempts_allowed'])
        name = quiz_data['name']

        cursor.close()
        conn.close()

        return Quiz(made_by, assigned_to_batch, assigned_to_semester, no_of_questions, total_marks, questions, last_date, number_of_attempts, quiz_id, name)

