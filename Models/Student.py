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

class student:
    def __init__(self, name, roll_no, password):
        self.name = name
        self.roll_no = roll_no
        self.password = password
        self.batch = self.get_batch()
        self.semester = self.get_semester()
        self.quizzes_assigned = []  # This should be loaded from the database
        self.responses = []  # This should be loaded from the database

    def get_batch(self):
        pass

    def get_semester(self):
        pass

    def get_quizzes_assigned(self):
        pass

    def get_responses(self):
        pass

    def add_response(self, response):
        pass

    def to_sql(self):
        pass

    def from_sql(self):
        pass

    def check_password(self, password):
        pass