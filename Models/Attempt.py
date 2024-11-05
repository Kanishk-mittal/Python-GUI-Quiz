import os
from dotenv import load_dotenv
from .Quiz import Quiz
from .Question import Question
import mysql.connector as msc
import matplotlib.pyplot as plt

class Attempt:
    """
    A class to represent an attempt made by a student on a quiz.

    Attributes:
    -----------
    student_roll_no : str
        The roll number of the student making the attempt.
    quiz_id : str
        The ID of the quiz being attempted.
    answers : list
        The list of answers provided by the student.
    time_stamp : str
        The timestamp when the attempt was made.
    id : int, optional
        The ID of the attempt (default is None, which generates a new ID).
    marks_obtained : int, optional
        The marks obtained in the attempt (default is None, which calculates the score).

    Methods:
    --------
    to_sql():
        Inserts the attempt data into the SQL database.
    from_sql(attempt_id):
        Retrieves an attempt from the SQL database using the attempt ID.
    get_score():
        Calculates the score of the attempt based on the answers provided.
    get_attempts(student_roll_no, quiz_id):
        Retrieves all attempts made by a student for a specific quiz.
    get_next_id():
        Retrieves the next available ID for a new attempt.
    __str__():
        Returns a string representation of the attempt.
    """
    def __init__(self, student_roll_no, quiz_id, answers, time_stamp,id=None,marks_obtained=None):
        """
        Initializes an Attempt instance.

        Parameters:
        student_roll_no (int): The roll number of the student.
        quiz_id (int): The ID of the quiz.
        answers (list): The list of answers provided by the student.
        time_stamp (datetime): The timestamp when the attempt was made.
        id (int, optional): The ID of the attempt. Defaults to None.
        marks_obtained (float, optional): The marks obtained in the attempt. Defaults to None.

        Attributes:
        id (int): The ID of the attempt.
        student_roll_no (int): The roll number of the student.
        quiz_id (int): The ID of the quiz.
        answers (list): The list of answers provided by the student.
        marks_obtained (float): The marks obtained in the attempt.
        time_stamp (datetime): The timestamp when the attempt was made.
        """
        if id is None:
            self.id = Attempt.get_next_id()
        self.student_roll_no = student_roll_no
        self.quiz_id = quiz_id
        self.answers = eval(answers)
        if marks_obtained is None:
            self.marks_obtained = self.get_score()
        else:
            self.marks_obtained = marks_obtained
        self.time_stamp = time_stamp
    def to_sql(self):
        """
        Inserts the attempt data into the 'attempts' table in the 'quiz_system' database.

        This method retrieves the SQL password from the environment variables, establishes a connection
        to the MySQL database, and executes an SQL INSERT statement to add the attempt data.

        Attributes:
            self.id (str): The ID of the attempt.
            self.student_roll_no (str): The roll number of the student.
            self.quiz_id (str): The ID of the quiz.
            self.answers (str): The answers provided by the student.
            self.marks_obtained (int): The marks obtained by the student.
            self.time_stamp (str): The timestamp of the attempt.

        Raises:
            mysql.connector.Error: If there is an error connecting to the database or executing the SQL statement.
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
        Retrieve an Attempt object from the database using the given attempt_id.

        Args:
            attempt_id (str): The ID of the attempt to retrieve.

        Returns:
            Attempt: An Attempt object containing the details of the retrieved attempt.

        Raises:
            mysql.connector.Error: If there is an error connecting to the database or executing the query.
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
        return Attempt(student_roll_no=attempt[0], quiz_id=attempt[1], answers=attempt[2], marks_obtained=attempt[3], time_stamp=attempt[4], id=attempt_id)

    def get_score(self):
        """
        Calculates and returns the total score for the quiz based on the user's answers.

        The method retrieves the quiz details from the database using the quiz ID,
        calculates the total score by iterating through each question and summing
        the scores based on the user's answers.

        Returns:
            int: The total score obtained by the user for the quiz.
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
        Retrieve attempts made by a student for a specific quiz.
        Args:
            student_roll_no (str): The roll number of the student.
            quiz_id (str): The ID of the quiz.
        Returns:
            list: A list of Attempt objects corresponding to the attempts made by the student for the specified quiz.
        Raises:
            Exception: If there is an issue connecting to the database or executing the query.
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
    @staticmethod
    def get_next_id():
        """
        Retrieves the next available attempt ID from the 'attempt' table in the 'quiz_system' database.

        This function connects to a MySQL database using credentials stored in environment variables,
        executes a query to find the maximum ID in the 'attempt' table, and returns the next ID by
        incrementing the maximum ID by 1.

        Returns:
            int: The next available attempt ID.

        Raises:
            mysql.connector.Error: If there is an error connecting to the database or executing the query.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT MAX(id) FROM attempt")
        attempt_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return attempt_id + 1
    def __str__(self):
        """
        Returns a string representation of the Attempt object.

        The string includes the Attempt ID, Student Roll No, Quiz ID, Answers,
        Marks Obtained, and Time Stamp.

        Returns:
            str: A formatted string containing the details of the Attempt object.
        """
        return f"Attempt ID: {self.id}\nStudent Roll No: {self.student_roll_no}\nQuiz ID: {self.quiz_id}\nAnswers: {self.answers}\nMarks Obtained: {self.marks_obtained}\nTime Stamp: {self.time_stamp}"
    
    def get_pie(self):
        """
        Creates a pie chart of the attempt results with the following sections:
        Correct Answers, Incorrect Answers, Unanswered Questions.
        """
        quiz = Quiz.from_sql(self.quiz_id)
        questions = {str(question.question_id): question.answer for question in quiz.questions}
        correct = 0
        incorrect = 0
        unanswered = 0
        print(self.answers)
        print(questions)

        for question_id, answer in self.answers.items():
            if answer == questions[question_id]:
                correct += 1
            elif answer == "":
                unanswered += 1
            else:
                incorrect += 1
        # creating pie chart
        labels = ['Correct Answers', 'Incorrect Answers', 'Unanswered Questions']
        sizes = [correct, incorrect, unanswered]
        colors = ['green', 'red', 'yellow']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')
        ax1.legend(labels, loc="lower right", bbox_to_anchor=(1, 0))
        return fig1