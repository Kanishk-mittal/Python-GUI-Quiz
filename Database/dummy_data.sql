use quiz_system;
-- Insert dummy data for Student
INSERT INTO Student (roll_no, name, password, batch_id, semester) VALUES
(2023BCY0001, 'Alice', 'password1', 1, 2023),
(2023BCY0002, 'Bob', 'password2', 2, 2023),
(2023BCY0003, 'Charlie', 'password3', 3, 2023),
(2023BCY0004, 'David', 'password4', 1, 2023),
(2023BCY0005, 'Eve', 'password5', 2, 2023);

-- Insert dummy data for Teacher
INSERT INTO Teacher (id, name, username, password) VALUES
(1, 'Prof. Smith', 'smith', 'password1'),
(2, 'Prof. Johnson', 'johnson', 'password2'),
(3, 'Prof. Williams', 'williams', 'password3'),
(4, 'Prof. Brown', 'brown', 'password4'),
(5, 'Prof. Jones', 'jones', 'password5');

-- Insert dummy data for Quiz
INSERT INTO Quiz (id, name, batch_id, semester, no_of_questions, last_date, teacher_id) VALUES
(1, 'Math Quiz', 1, 2023, 10, '2023-12-01', 1),
(2, 'Science Quiz', 2, 2023, 10, '2023-12-02', 2),
(3, 'History Quiz', 3, 2023, 10, '2023-12-03', 3),
(4, 'Geography Quiz', 1, 2023, 10, '2023-12-04', 4),
(5, 'English Quiz', 2, 2023, 10, '2023-12-05', 5);

-- Insert dummy data for Question
INSERT INTO Question (id, quiz_id, question, options, correct_answer, marks, type) VALUES
(1, 1, 'What is 2+2?', '{"a": "3", "b": "4", "c": "5", "d": "6"}', 'b', 1, 'MCQ'),
(2, 1, 'What is 3+5?', '{"a": "7", "b": "8", "c": "9", "d": "10"}', 'b', 1, 'MCQ'),
(3, 1, 'What is 5+5?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(4, 1, 'What is 6+4?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(5, 1, 'What is 7+3?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(6, 1, 'What is 8+2?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(7, 1, 'What is 9+1?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(8, 1, 'What is 10+0?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(9, 1, 'What is 11-1?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(10, 1, 'What is 12-2?', '{"a": "9", "b": "10", "c": "11", "d": "12"}', 'b', 1, 'MCQ'),
(11, 2, 'What is H2O?', '{"a": "Water", "b": "Oxygen", "c": "Hydrogen", "d": "Carbon Dioxide"}', 'a', 1, 'MCQ'),
(12, 2, 'What is CO2?', '{"a": "Water", "b": "Oxygen", "c": "Hydrogen", "d": "Carbon Dioxide"}', 'd', 1, 'MCQ'),
(13, 2, 'What is the chemical symbol for Gold?', '{"a": "Au", "b": "Ag", "c": "Pb", "d": "Fe"}', 'a', 1, 'MCQ'),
(14, 2, 'What is the chemical symbol for Silver?', '{"a": "Au", "b": "Ag", "c": "Pb", "d": "Fe"}', 'b', 1, 'MCQ'),
(15, 2, 'What is the chemical symbol for Iron?', '{"a": "Au", "b": "Ag", "c": "Pb", "d": "Fe"}', 'd', 1, 'MCQ'),
(16, 2, 'What is the chemical symbol for Lead?', '{"a": "Au", "b": "Ag", "c": "Pb", "d": "Fe"}', 'c', 1, 'MCQ'),
(17, 2, 'What is the chemical symbol for Oxygen?', '{"a": "O", "b": "O2", "c": "O3", "d": "O4"}', 'a', 1, 'MCQ'),
(18, 2, 'What is the chemical symbol for Nitrogen?', '{"a": "N", "b": "N2", "c": "N3", "d": "N4"}', 'a', 1, 'MCQ'),
(19, 2, 'What is the chemical symbol for Carbon?', '{"a": "C", "b": "C2", "c": "C3", "d": "C4"}', 'a', 1, 'MCQ'),
(20, 2, 'What is the chemical symbol for Helium?', '{"a": "He", "b": "H", "c": "H2", "d": "H3"}', 'a', 1, 'MCQ'),
(21, 3, 'Who was the first President of the United States?', '{"a": "George Washington", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(22, 3, 'Who wrote the Declaration of Independence?', '{"a": "George Washington", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'b', 1, 'MCQ'),
(23, 3, 'Who was the 16th President of the United States?', '{"a": "George Washington", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'c', 1, 'MCQ'),
(24, 3, 'Who was the second President of the United States?', '{"a": "George Washington", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'd', 1, 'MCQ'),
(25, 3, 'Who was the third President of the United States?', '{"a": "George Washington", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'b', 1, 'MCQ'),
(26, 3, 'Who was the fourth President of the United States?', '{"a": "James Madison", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(27, 3, 'Who was the fifth President of the United States?', '{"a": "James Monroe", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(28, 3, 'Who was the sixth President of the United States?', '{"a": "John Quincy Adams", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(29, 3, 'Who was the seventh President of the United States?', '{"a": "Andrew Jackson", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(30, 3, 'Who was the eighth President of the United States?', '{"a": "Martin Van Buren", "b": "Thomas Jefferson", "c": "Abraham Lincoln", "d": "John Adams"}', 'a', 1, 'MCQ'),
(31, 4, 'What is the capital of France?', '{"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(32, 4, 'What is the capital of Germany?', '{"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"}', 'c', 1, 'MCQ'),
(33, 4, 'What is the capital of Spain?', '{"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"}', 'd', 1, 'MCQ'),
(34, 4, 'What is the capital of Italy?', '{"a": "Rome", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(35, 4, 'What is the capital of the United Kingdom?', '{"a": "Paris", "b": "London", "c": "Berlin", "d": "Madrid"}', 'b', 1, 'MCQ'),
(36, 4, 'What is the capital of Portugal?', '{"a": "Lisbon", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(37, 4, 'What is the capital of Greece?', '{"a": "Athens", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(38, 4, 'What is the capital of Russia?', '{"a": "Moscow", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(39, 4, 'What is the capital of Japan?', '{"a": "Tokyo", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(40, 4, 'What is the capital of China?', '{"a": "Beijing", "b": "London", "c": "Berlin", "d": "Madrid"}', 'a', 1, 'MCQ'),
(41, 5, 'What is the synonym of "happy"?', '{"a": "Sad", "b": "Joyful", "c": "Angry", "d": "Tired"}', 'b', 1, 'MCQ'),
(42, 5, 'What is the antonym of "big"?', '{"a": "Small", "b": "Large", "c": "Huge", "d": "Gigantic"}', 'a', 1, 'MCQ'),
(43, 5, 'What is the synonym of "fast"?', '{"a": "Slow", "b": "Quick", "c": "Lazy", "d": "Tired"}', 'b', 1, 'MCQ'),
(44, 5, 'What is the antonym of "hot"?', '{"a": "Cold", "b": "Warm", "c": "Boiling", "d": "Scorching"}', 'a', 1, 'MCQ'),
(45, 5, 'What is the synonym of "smart"?', '{"a": "Dumb", "b": "Intelligent", "c": "Stupid", "d": "Foolish"}', 'b', 1, 'MCQ'),
(46, 5, 'What is the antonym of "early"?', '{"a": "Late", "b": "Soon", "c": "Prompt", "d": "Punctual"}', 'a', 1, 'MCQ'),
(47, 5, 'What is the synonym of "strong"?', '{"a": "Weak", "b": "Powerful", "c": "Feeble", "d": "Fragile"}', 'b', 1, 'MCQ'),
(48, 5, 'What is the antonym of "light"?', '{"a": "Heavy", "b": "Bright", "c": "Luminous", "d": "Radiant"}', 'a', 1, 'MCQ'),
(49, 5, 'What is the synonym of "brave"?', '{"a": "Cowardly", "b": "Courageous", "c": "Fearful", "d": "Timid"}', 'b', 1, 'MCQ'),
(50, 5, 'What is the antonym of "rich"?', '{"a": "Poor", "b": "Wealthy", "c": "Affluent", "d": "Prosperous"}', 'a', 1, 'MCQ');


-- Insert dummy data for Attempt
INSERT INTO Attempt (id, student_roll_no, quiz_id, answers, marks_obtained, time_stamp) VALUES
(1, 2023BCY0001, 1, '{"1": "b", "2": "b", "3": "b", "4": "b", "5": "b", "6": "b", "7": "b", "8": "b", "9": "b", "10": "b"}', 10, '2023-12-01 10:00:00'),
(3, 2023BCY0003, 3, '{"21": "a", "22": "b", "23": "c", "24": "d", "25": "b", "26": "a", "27": "a", "28": "a", "29": "a", "30": "a"}', 10, '2023-12-03 10:00:00'),
(4, 2023BCY0004, 4, '{"31": "a", "32": "c", "33": "d", "34": "a", "35": "b", "36": "a", "37": "a", "38": "a", "39": "a", "40": "a"}', 10, '2023-12-04 10:00:00'),
(5, 2023BCY0005, 5, '{"41": "b", "42": "a", "43": "b", "44": "a", "45": "b", "46": "a", "47": "b", "48": "a", "49": "b", "50": "a"}', 10, '2023-12-05 10:00:00'),
(6, 2023BCY0001, 2, '{"11": "a", "12": "d", "13": "a", "14": "b", "15": "d", "16": "c", "17": "a", "18": "a", "19": "a", "20": "a"}', 10, '2023-12-06 10:00:00'),
(7, 2023BCY0002, 3, '{"21": "a", "22": "b", "23": "c", "24": "d", "25": "b", "26": "a", "27": "a", "28": "a", "29": "a", "30": "a"}', 10, '2023-12-07 10:00:00')
;