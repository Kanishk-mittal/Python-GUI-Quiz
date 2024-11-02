import matplotlib.pyplot as plt
import mysql.connector as msc
import dotenv
import os
import nltk

dotenv.load_dotenv()

class Question:
    def __init__(self, statement=None, type=None, options=None, marks=None, question_id=None, answer=None):
        self.question = statement
        self.type = type
        self.options = eval(options)
        self.marks = marks
        self.question_id = question_id
        self.answer = answer
    def __str__(self):
        return f"Question ID: {self.question_id}\nQuestion: {self.question}\nType: {self.type}\nOptions: {self.options}\nMarks: {self.marks}\nAnswer: {self.answer}"
    
    def to_sql(self):
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
        if self.type == 'MCQ':
            if response == self.answer:
                return self.marks
            else:
                return 0
        elif self.type == 'Short Answer':
            if response.lower() == self.answer.lower():
                return self.marks
            else:
                return 0
        elif self.type == 'Long Answer':
            """
            This function will remove all stopwords and normalise words from the response and the answer and then calculate the similarity between the two.
            """
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

    def pie(self):
        """
        This function will load all responses and create a pie chart of the responses denoting the percentage of each response and those who did not respond.
        """
        pass

