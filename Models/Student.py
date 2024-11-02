"""
This file contains the Student class which is used to represent a student in the system.

Attributes:
    1. Name (str): The name of the student.
    2. roll_no (str): The roll number of the student.
    3. batch (str): The batch to which the student belongs. (calculated from roll_no)
    4. semester (str): The semester in which the student is enrolled. (calculated from roll_no)
    5. password (str): The password of the student. 
    6. quizzes_assigned (list): A list of quizzes assigned to the student. (load from database)
    7. responses (list): A list of responses submitted by the student. (load from database)

Methods:
    1. constructor: Initializes the student object with the given attributes.
    2. get_batch: Returns the batch of the student.
    3. get_semester: Returns the semester of the student.
    4. get_quizzes_assigned: Returns the list of quizzes assigned to the student.
    5. get_responses: Returns the list of responses submitted by the student.
    6. add_response: Adds a response to the list of responses.
    7. to_sql: Saves the student object to the database.
    8. from_sql: Loads the student object from the database.
    9. Check_password: Checks if the given password is correct.
"""

import mysql.connector as msc
from dotenv import load_dotenv
from .Quiz import Quiz
from .Attempt import Attempt
import os
import matplotlib.pyplot as plt

load_dotenv()

class student:
    def __init__(self, name, roll_no, password):
        self.name = name
        self.roll_no = roll_no
        self.password = password
        self.batch = self.get_batch()
        self.semester = self.get_semester()
        self.quizzes_assigned = self.load_quizzes()
        self.responses = self.load_responses()
    def get_batch(self):
        batch= int(self.roll_no[-3:])%3
        if batch==0:
            batch=3
        return batch
    def get_semester(self):
        return self.roll_no[:4]
    def load_quizzes(self):
        return Quiz.get_quizzes(self.batch,self.semester)
    def load_responses(self):
        quiz_ids = [quiz.quiz_id for quiz in self.quizzes_assigned]
        responses = []
        for quiz_id in quiz_ids:
            responses+=Attempt.get_attempts(self.roll_no,quiz_id)
        print(responses)
        return responses
    def get_pie(self):
        """
        This function return a matplotlib plot of the percentage of quizzes attempted by the student.
        """
        attempted_quizzes = set(response.quiz_id for response in self.responses)
        total_quizzes = len(self.quizzes_assigned)
        labels = ['Attempted','Not Attempted']
        sizes = [len(attempted_quizzes),total_quizzes-len(attempted_quizzes)]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        return fig1
    def mini_report(self):
        """
        return a dictionary with keys as no_of_attempts, avg_percentage
        """
        no_of_attempts = len(self.responses)
        total_marks = 0
        marks_obtained = 0
        for response in self.responses:
            total_marks += Quiz.from_sql(response.quiz_id).total_marks
            marks_obtained += response.marks_obtained
        avg_percentage = marks_obtained / total_marks * 100
        return {'no_of_attempts': no_of_attempts, 'avg_percentage': avg_percentage}
    @staticmethod
    def from_sql(roll_no):
        """
        This function will return the student object from the database.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, password FROM student WHERE roll_no = '{roll_no}'")
        student_data = cursor.fetchone()
        cursor.close()
        conn.close()
        return student(student_data[0], roll_no, student_data[1])
