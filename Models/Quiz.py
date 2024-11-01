"""
This file contains the Quiz class which is used to store the details of a quiz
and perform operations on it.
Attributes:
    1. made_by (Teacher): The teacher who created the quiz.
    2. assigned_to_batch (str): The batch to which the quiz is assigned.
    3. assigend_to_semester (str): The semester to which the quiz is assigned.
    4. no_of_questions (int): The number of questions in the quiz.
    5. Total_marks (int): The total marks of the quiz.
    6. questions (list): A list of Question objects.
    7. last_date (datetime): The last date and time to submit the quiz.
    8. number_of_attempts (int): The number of attempts allowed for the quiz.
    9. quiz_id (str): The unique id of the quiz.
    10. name (str): The name of the quiz.
Methods:
    1. constructor(made_by, assigned_to_batch, assigned_to_semester, no_of_questions, total_marks, questions, last_date, number_of_attempts, quiz_id):
        Initializes the Quiz object with the given parameters.
    2. to_sql():
        Saves the quiz details to the database.
    3. from_sql(quiz_id):
        Retrieves the quiz details from the database.
    4. update():
        Updates the quiz details in the database.
    5. delete():
        Deletes the quiz from the database.
    6. add_question(question):
        Adds a question to the quiz.
    7. remove_question(question_id):
        Removes a question from the quiz.
    8. percent_attempted():
        Returns the percentage of students who have attempted the quiz.
    9. get_all_responses():
        Returns the responses of all students for the quiz.
    10. get_response(student_id):
        Returns the response of a student for the quiz.
    11. get_report():
        Returns the report of the quiz.
    12. get_individual_report(student_id):
        Returns the report of a student for the quiz.
    13. attempts_left(student_id):
        Returns the number of attempts left for a student.
    
"""
import dotenv
import os
from .Teacher import Teacher
from .Question import Question
import mysql.connector as msc

class Quiz:
    def __init__(self, made_by, assigned_to_batch, assigned_to_semester, no_of_questions, total_marks, questions, last_date, number_of_attempts, quiz_id, name):
        self.made_by = made_by
        self.assigned_to_batch = assigned_to_batch
        self.assigned_to_semester = assigned_to_semester
        self.no_of_questions = no_of_questions
        self.total_marks = total_marks
        self.questions = questions
        self.last_date = last_date
        self.number_of_attempts = number_of_attempts
        self.quiz_id = quiz_id
        self.name = name    

    def to_sql(self):
        pass

    def from_sql(self, quiz_id):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def add_question(self, question):
        pass

    def remove_question(self, question_id):
        pass

    def percent_attempted(self):
        pass

    def get_all_responses(self):
        pass

    def get_response(self, student_id):
        pass

    def get_report(self):
        pass

    def get_individual_report(self, student_id):
        pass
    
    def attempts_left(self, student_id):
        return self.number_of_attempts