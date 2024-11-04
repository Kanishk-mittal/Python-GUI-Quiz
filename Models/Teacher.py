import mysql.connector as msc
from dotenv import load_dotenv
from Models.Quiz import Quiz
import os

load_dotenv()

class Teacher:
    def __init__(self, name, username, password, id=None):  
        if id:
            self.id = id
        else:
            self.id=Teacher.get_next_id()
        self.name = name
        self.username = username
        self.password = password
        self.quizzes = self.load_quizzes()
    @staticmethod   
    def get_next_id():
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) FROM teacher")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result[0] + 1 if result[0] else 1
    def load_quizzes(self): 
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()
        cursor.execute(f"SELECT id FROM quiz WHERE teacher_id = {self.id}")
        print(f"SELECT id FROM quiz WHERE teacher_id = {self.id}")
        result = cursor.fetchall()
        quizzes = []
        for row in result:
            quizzes.append(Quiz.from_sql(row[0]))
        cursor.close()
        connection.close()
        return quizzes
    def get_teacher_by_username(username):
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM teacher WHERE username = '{username}'")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return Teacher(result[1], result[2], result[3], result[0])

