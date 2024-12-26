CREATE DATABASE quiz_system;
USE quiz_system;

CREATE TABLE Student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    batch_id INT,
    semester INT
);

CREATE TABLE Teacher (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Quiz (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    batch_id INT,
    semester INT,
    no_of_questions INT,
    last_date DATE,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(id)
);

CREATE TABLE Question (
    id INT PRIMARY KEY,
    quiz_id INT,
    question TEXT,
    options JSON,
    correct_answer VARCHAR(255),
    marks INT,
    type VARCHAR(50),
    FOREIGN KEY (quiz_id) REFERENCES Quiz(id)
);

CREATE TABLE Attempt (
    id INT PRIMARY KEY,
    student_roll_no INT,
    quiz_id INT,
    answers JSON,
    marks_obtained INT,
    time_stamp DATETIME,
    FOREIGN KEY (student_roll_no) REFERENCES Student(roll_no),
    FOREIGN KEY (quiz_id) REFERENCES Quiz(id)
);