# Quiz System

This project is a Quiz System built using Python. It allows teachers to create quizzes and students to attempt them. The system includes functionalities for user authentication, quiz creation, quiz attempts, and result analysis.

## Features

- **User Authentication**: Separate login for students and teachers.
- **Quiz Creation**: Teachers can create quizzes with multiple types of questions (MCQ, Short Answer, Long Answer).
- **Quiz Attempt**: Students can attempt quizzes assigned to them.
- **Result Analysis**: Students can view their quiz results and teachers can analyze quiz performance.

## Project Structure

```
Python Project/
│
├── Database/
│   ├── creation_script.sql
│   ├── Creator.py
│   ├── dummy_data.sql
│   ├── DummyData/
│   │   ├── attempt.csv
│   │   ├── question.csv
│   │   ├── quiz.csv
│   │   ├── student.csv
│   │   └── teacher.csv
│   └── __init__.py
│
├── Models/
│   ├── Attempt.py
│   ├── Question.py
│   ├── Quiz.py
│   ├── Student.py
│   ├── Teacher.py
│   └── __init__.py
│
├── UI/
│   ├── Add_question.py
│   ├── Components/
│   │   ├── Add_mcq_question.py
│   │   ├── Add_short_answer_question.py
│   │   ├── Add_long_answer_question.py
│   │   ├── MCQ_question.py
│   │   ├── Long_answer_question.py
│   │   ├── Short_answer_question.py
│   │   ├── Student_quiz_card.py
│   │   ├── Teacher_quiz_card.py
│   │   └── __init__.py
│   ├── Login.py
│   ├── Register.py
│   ├── Student_dashboard.py
│   ├── Student_quiz_review.py
│   ├── Quiz_attempt.py
│   ├── Teacher_Dashboard.py
│   └── __init__.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/quiz-system.git
    cd quiz-system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Ensure you have MySQL installed and running.
    - Create a `.env` file in the root directory and add your MySQL password:
      ```
      SQL_PASSWORD=your_mysql_password
      ```
    - Run the database creation script:
      ```sh
      python Database/Creator.py
      ```

5. Run the application:
    ```sh
    python main.py
    ```

## Usage

- **Login**: Use the login window to log in as a student or teacher.
- **Register**: If you don't have an account, use the register option to create a new account.
- **Teacher Dashboard**: Teachers can create quizzes and view quiz performance.
- **Student Dashboard**: Students can view and attempt quizzes assigned to them.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please contact [your email].
