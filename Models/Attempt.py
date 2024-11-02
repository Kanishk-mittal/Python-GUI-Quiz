import os
from dotenv import load_dotenv
from .Quiz import Quiz
from .Question import Question
import mysql.connector as msc



class Attempt:
    """
    This class will have following attributes:
    id
    student_roll_no
    quiz_id
    answers
    marks_obtained
    time_stamp
    """
    def __init__(self, id, student_roll_no, quiz_id, answers, marks_obtained, time_stamp):
        self.id = id
        self.student_roll_no = student_roll_no
        self.quiz_id = quiz_id
        self.answers = answers
        self.marks_obtained = marks_obtained
        self.time_stamp = time_stamp
    def to_sql(self):
        """
        This function will save the attempt object to the database.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO attempts (id, student_roll_no, quiz_id, answers, marks_obtained, time_stamp) VALUES ('{self.id}','{self.student_roll_no}', '{self.quiz_id}', '{self.answers}', {self.marks_obtained}, '{self.time_stamp}')")
        cursor.close()
        conn.close()
    @staticmethod
    def from_sql(attempt_id):
        """
        This function will return the attempt object from the database.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT student_roll_no, quiz_id, answers, marks_obtained, time_stamp FROM attempt WHERE id = '{attempt_id}'")
        attempt = cursor.fetchone()
        cursor.close()
        conn.close()
        return Attempt(attempt_id, attempt[0], attempt[1], attempt[2], attempt[3], attempt[4])
    def get_score(self):
        """
        This function will calculate the score of the attempt.
        """
        quiz = Quiz.from_sql(self.quiz_id)
        total_marks = quiz.total_marks
        questions = quiz.questions
        score = 0
        for i in range(len(questions)):
            score += questions[i].get_score(self.answers[i])
        return score
    @staticmethod
    def get_attempts(student_roll_no, quiz_id):
        """
        This function will return all the attempts of a student for a quiz.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM attempt WHERE student_roll_no = '{student_roll_no}' AND quiz_id = '{quiz_id}'")
        attempts = []
        for attempt_id in cursor.fetchall():
            attempts.append(Attempt.from_sql(attempt_id[0]))
        cursor.close()
        conn.close()
        return attempts