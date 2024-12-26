import mysql.connector as msc
from dotenv import load_dotenv
from Models.Quiz import Quiz
import os

load_dotenv()

class Teacher:
    def __init__(self, name, username, password,email, id=None):  
        if id:
            self.id = id
        else:
            self.id=Teacher.get_next_id()
        self.name = name
        self.username = username
        self.password = password
        self.quizzes = self.load_quizzes()
        self.email = email
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
        cursor = connection.cursor(buffered=True)
        cursor.execute(f"SELECT id FROM quiz WHERE teacher_id = {self.id}")
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
        cursor.execute(f"SELECT id,name,username,password,email_id FROM teacher WHERE username = '{username}'")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return Teacher(
                id=result[0],
                name=result[1],
                username=result[2],
                password=result[3],
                email=result[4]
            )
    def to_sql(self):
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO teacher (id, name, username, password,email_id) VALUES ({self.id}, '{self.name}', '{self.username}', '{self.password}','{self.email}')")
        connection.commit()
        cursor.close()
        connection.close()
    def remove_quiz(self, quiz):
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM quiz WHERE id = {quiz.quiz_id}")
        connection.commit()
        cursor.close()
        connection.close()
    def update(self):
        # This funtion updates the object from the database
        connection = msc.connect(
            host="localhost",
            user="root",
            password=os.getenv("SQL_PASSWORD"),
            database="quiz_system")
        cursor = connection.cursor()

    @staticmethod
    def verify(username,password):
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT username FROM teacher WHERE username = '{username}' AND password = '{password}'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return Teacher.get_teacher_by_username(username=username)
        else:
            return False


