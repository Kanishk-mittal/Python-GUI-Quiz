import customtkinter as ctk
from UI.Components.MCQ_question import McqQuestion
from UI.Components.Short_answer_question import ShortAnswerQuestion
from UI.Components.Long_answer_question import LongAnswerQuestion
from Models.Quiz import Quiz
from Models.Attempt import Attempt  
from Models.Student import student
from datetime import datetime
from tkinter.messagebox import showinfo

class QuizAttempt(ctk.CTkToplevel):
    def __init__(self, master, student, quiz):
        super().__init__(master)
        self.quiz = quiz
        self.student=student
        self.title("Quiz Attempt")
        self.geometry("800x600")

        # Display student name
        self.student_name_label = ctk.CTkLabel(self, text=student.name, font=("Arial", 24))
        self.student_name_label.pack(pady=10)

        # Display quiz name
        self.quiz_name_label = ctk.CTkLabel(self, text=quiz.name, font=("Arial", 24))
        self.quiz_name_label.pack(pady=10)

        # Display quiz creator
        self.quiz_creator_label = ctk.CTkLabel(self, text=f"Created by: {quiz.made_by}", font=("Arial", 14))
        self.quiz_creator_label.pack(pady=5)

        # Container for questions
        self.questions_frame = ctk.CTkScrollableFrame(self,bg_color="white")
        self.questions_frame.pack(pady=20, fill="both", expand=True)

        self.answers = {}

        for question in quiz.questions:
            if question.type == "MCQ":
                question_widget = McqQuestion(self.questions_frame, question)
                question_widget.pack(pady=10, expand=True, fill="both")
            elif question.type == "Short Answer":
                question_widget = ShortAnswerQuestion(self.questions_frame, question)
                question_widget.pack(pady=10, expand=True, fill="both")
            elif question.type == "Long Answer":
                question_widget = LongAnswerQuestion(self.questions_frame, question)
                question_widget.pack(pady=10, expand=True, fill="both")

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        answers = dict()
        for question_widget in self.questions_frame.winfo_children():
            question_id, answer = question_widget.get_answer()
            answers[question_id] = answer
        attempt=Attempt(self.student.roll_no,self.quiz.quiz_id,answers,datetime.now())
        attempt.to_sql()
        showinfo("Success", "Quiz submitted successfully")
        self.destroy()


if __name__ == "__main__":
    from Models.Question import Question
    from Models.Quiz import Quiz
    from Models.Attempt import Attempt
    from Models.Student import student

    quiz = Quiz.from_sql(2)

    student = student.from_sql("2023BCY0001")   
    root=ctk.CTk()
    quiz_attempt = QuizAttempt(root, student, quiz)
    root.mainloop()
