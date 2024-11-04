import matplotlib.pyplot as plt
import mysql.connector as msc
import dotenv
import os
import nltk

dotenv.load_dotenv()

class Question:
    """
    A class to represent a question in a quiz system.
    Attributes:
    ----------
    statement : str
        The text of the question.
    typ : str
        The type of the question (e.g., 'MCQ', 'Short Answer', 'Long Answer').
    options : list
        The list of options for the question (used for MCQ type).
    marks : int
        The marks assigned to the question.
    question_id : int
        The unique identifier for the question.
    answer : str
        The correct answer for the question.
    Methods:
    -------
    __str__():
        Returns a string representation of the question.
    to_sql():
        Inserts the question into the SQL database.
    from_sql(question_id):
        Retrieves a question from the SQL database using the question_id.
    get_score(response):
        Calculates the score for a given response based on the type of question.
    pie():
        Generates a pie chart of the responses to the question.
    """
    def __init__(self, statement=None, typ=None, options=None, marks=None, question_id=None, answer=None):
        """
        Initializes a new instance of the Question class.

        Parameters:
        statement (str, optional): The text of the question.
        typ (str, optional): The type of the question (e.g., multiple choice, true/false).
        options (str, optional): A string representation of the list of options for the question.
        marks (int, optional): The marks assigned to the question.
        question_id (int, optional): The unique identifier for the question.
        answer (str, optional): The correct answer to the question.
        """
        self.question = statement
        self.type = typ
        self.options = eval(options)
        self.marks = marks
        self.question_id = question_id
        self.answer = answer
    def __str__(self):
        return f"Question ID: {self.question_id}\nQuestion: {self.question}\nType: {self.type}\nOptions: {self.options}\nMarks: {self.marks}\nAnswer: {self.answer}"
    
    def to_sql(self):
        """
        Inserts the question data into the SQL database.

        This method connects to a MySQL database using credentials from environment variables,
        and inserts the question details into the 'questions' table.

        Raises:
            mysql.connector.Error: If there is an error connecting to the database or executing the SQL query.
        """
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        conn = msc.connect(
            host="localhost",
            user="root",
            password=SQL_PASSWORD,
            database="quiz"
        )
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO questions (question_id, question, type, options, marks, answer) VALUES ('{self.question_id}','{self.question}', '{self.type}', '{self.options}', {self.marks}, '{self.answer}')")
        cursor.close()
        conn.close()
    @staticmethod  
    def from_sql(question_id):
        """
        Retrieve a question from the database using its ID.

        Args:
            question_id (int): The ID of the question to retrieve.

        Returns:
            Question: An instance of the Question class containing the question details.

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
        cursor.execute(f"SELECT question, type, options, marks, correct_answer FROM question WHERE id = '{question_id}'")
        question = cursor.fetchone()
        cursor.close()
        conn.close()
        return Question(question[0], question[1], question[2], question[3], question_id, question[4])
    
    def get_score(self, response):
        """
        Calculate the score for a given response based on the question type.

        Parameters:
        response (str): The response provided by the user.

        Returns:
        int: The score based on the response and question type.

        Question Types:
        - 'MCQ': Multiple Choice Questions. Full marks if the response matches the correct option.
        - 'Short Answer': Case-insensitive comparison of the response with the correct answer.
        - 'Long Answer': Calculates similarity by removing stopwords, normalizing words, and comparing the response with the correct answer.

        Note:
        For 'Long Answer' type, the similarity is calculated as:
        (number of common words / total unique words) * marks
        """
        if self.type == 'MCQ':
            if response == self.options[self.answer] or response == self.answer:
                return self.marks
            else:
                return 0
        elif self.type == 'Short Answer':
            if response.lower() == self.answer.lower():
                return self.marks
            else:
                return 0
        elif self.type == 'Long Answer':
            # Tokenize the response and the answer
            response_tokens = nltk.word_tokenize(response)
            answer_tokens = nltk.word_tokenize(self.answer)
            # Remove stopwords
            response_tokens = [word for word in response_tokens if word not in nltk.corpus.stopwords.words('english')]
            answer_tokens = [word for word in answer_tokens if word not in nltk.corpus.stopwords.words('english')]
            # Normalise the words
            response_tokens = [nltk.PorterStemmer().stem(word) for word in response_tokens]
            answer_tokens = [nltk.PorterStemmer().stem(word) for word in answer_tokens]
            # returning marks * (no of common words / total words)
            return self.marks * len(set(response_tokens).intersection(set(answer_tokens))) / len(set(response_tokens).union(set(answer_tokens))) 
        else:
            return 0

