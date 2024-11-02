import customtkinter as ctk
from Components.MCQ_question import McqQuestion
from Components.Short_answer_question import ShortAnswerQuestion
from Components.Long_answer_question import LongAnswerQuestion
from Models.Quiz import Quiz
from Models.Attempt import Attempt  

class QuizAttempt(ctk.CTkToplevel):
    def __init__(self, master, student_name, quiz: Quiz):
        super().__init__(master)
        self.title("Quiz Attempt")
        self.geometry("800x600")

        # Display student name
        self.student_name_label = ctk.CTkLabel(self, text=student_name, font=("Arial", 24))
        self.student_name_label.pack(pady=10)

        # Display quiz name
        self.quiz_name_label = ctk.CTkLabel(self, text=quiz.name, font=("Arial", 24))
        self.quiz_name_label.pack(pady=10)

        # Display quiz creator
        self.quiz_creator_label = ctk.CTkLabel(self, text=f"Created by: {quiz.creator}", font=("Arial", 14))
        self.quiz_creator_label.pack(pady=5)

        # Container for questions
        self.questions_frame = ctk.CTkFrame(self)
        self.questions_frame.pack(pady=20, fill="both", expand=True)

        self.answers = {}

        for question in quiz.questions:
            if isinstance(question, McqQuestion):
                self._add_mcq_question(question)
            elif isinstance(question, ShortAnswerQuestion):
                self._add_short_answer_question(question)
            elif isinstance(question, LongAnswerQuestion):
                self._add_long_answer_question(question)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def _add_mcq_question(self, question):
        frame = ctk.CTkFrame(self.questions_frame)
        frame.pack(pady=10, fill="x")

        label = ctk.CTkLabel(frame, text=question.text, font=("Arial", 14))
        label.pack(anchor="w")

        var = ctk.StringVar()
        for option in question.options:
            rb = ctk.CTkRadioButton(frame, text=option, variable=var, value=option)
            rb.pack(anchor="w")

        self.answers[question.id] = var

    def _add_short_answer_question(self, question):
        frame = ctk.CTkFrame(self.questions_frame)
        frame.pack(pady=10, fill="x")

        label = ctk.CTkLabel(frame, text=question.text, font=("Arial", 14))
        label.pack(anchor="w")

        entry = ctk.CTkEntry(frame)
        entry.pack(fill="x")

        self.answers[question.id] = entry

    def _add_long_answer_question(self, question):
        frame = ctk.CTkFrame(self.questions_frame)
        frame.pack(pady=10, fill="x")

        label = ctk.CTkLabel(frame, text=question.text, font=("Arial", 14))
        label.pack(anchor="w")

        text = ctk.CTkText(frame, height=5)
        text.pack(fill="x")

        self.answers[question.id] = text

    def submit(self):
        result = {}
        for question_id, widget in self.answers.items():
            if isinstance(widget, ctk.StringVar):
                result[question_id] = widget.get()
            elif isinstance(widget, ctk.CTkEntry):
                result[question_id] = widget.get()
            elif isinstance(widget, ctk.CTkText):
                result[question_id] = widget.get("1.0", "end").strip()
        print(result)
        self.destroy()