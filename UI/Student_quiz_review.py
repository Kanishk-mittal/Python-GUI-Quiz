import customtkinter as ctk
from Models.Quiz import Quiz
from Models.Attempt import Attempt
from Models.Student import student
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StudentQuizReview(ctk.CTkToplevel):
    """
    A class to represent the quiz review window for a student.
    Attributes
    ----------
    student : Student
        The student object containing student details.
    quiz : Quiz
        The quiz object containing quiz details.
    attempt : list
        A list of attempts made by the student for the quiz.
    Methods
    -------
    __init__(master, student, quiz):
        Initializes the StudentQuizReview window with the given master, student, and quiz.
    create_widgets():
        Creates and packs the widgets for the quiz review window.
    add_attempt(attempt, attempt_no):
        Adds the details of a specific attempt to the quiz review window.
    """
    def __init__(self, master, student, quiz):
        """
        Initializes the StudentQuizReview window.

        Args:
            master (tk.Tk): The parent window.
            student (Student): The student object containing student details.
            quiz (Quiz): The quiz object containing quiz details.
        """
        super().__init__(master)
        self.student = student
        self.quiz = quiz
        self.attempt = Attempt.get_attempts(student.roll_no, quiz.quiz_id)
        self.title("Quiz Review")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        """
        Create and pack the widgets for the student quiz review UI.
        This method initializes and packs the labels for the student's name and the quiz's name.
        It also iterates through the student's attempts and adds each attempt to the UI.
        Attributes:
            student_label (ctk.CTkLabel): Label displaying the student's name.
            quiz_label (ctk.CTkLabel): Label displaying the quiz's name.
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.student_label = ctk.CTkLabel(self.scrollable_frame, text=f"Student: {self.student.name}", font=("Arial", 16), anchor="w")

        self.quiz_label = ctk.CTkLabel(self.scrollable_frame, text=f"Quiz: {self.quiz.name}", font=("Arial", 16), anchor="w")

        self.student_label.pack(pady=10, fill="x")
        self.quiz_label.pack(pady=10, fill="x")

        for idx, attempt in enumerate(self.attempt):
            self.add_attempt(attempt, idx + 1)

    def add_attempt(self, attempt, attempt_no):
        """
        Adds an attempt review to the UI.
        This method creates a new section in the UI to display the details of a quiz attempt.
        It includes a pie chart of the attempt results, a table of questions with the user's answers,
        the correct answers, and the marks obtained for each question.
        Args:
            attempt (Attempt): An object representing the quiz attempt, containing the user's answers.
            attempt_no (int): The attempt number to be displayed in the UI.
        Returns:
            None
        """
        attempt_label = ctk.CTkLabel(self.scrollable_frame, text=f"Attempt-{attempt_no}")
        attempt_label.pack(pady=10)

        fig = attempt.get_pie()
        canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        table_frame = ctk.CTkScrollableFrame(self.scrollable_frame)
        table_frame.pack(pady=10, expand=True, fill="both")

        headers = ["Question ID", "Question", "Your Answer", "Correct Answer", "Marks Obtained"]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(table_frame, text=header)
            header_label.grid(row=0, column=col, padx=5, pady=5)

        for row, question in enumerate(self.quiz.questions, start=1):
            question_id_label = ctk.CTkLabel(table_frame, text=question.question_id)
            question_id_label.grid(row=row, column=0, padx=5, pady=5)

            question_text_label = ctk.CTkLabel(table_frame, text=question.question)
            question_text_label.grid(row=row, column=1, padx=5, pady=5)

            your_answer_label = ctk.CTkLabel(table_frame, text=question.options[attempt.answers[str(question.question_id)]])
            your_answer_label.grid(row=row, column=2, padx=5, pady=5)

            correct_answer_label = ctk.CTkLabel(table_frame, text=question.options[question.answer])
            correct_answer_label.grid(row=row, column=3, padx=5, pady=5)

            marks_obtained_label = ctk.CTkLabel(table_frame, text=question.get_score(attempt.answers[str(question.question_id)]))
            marks_obtained_label.grid(row=row, column=4, padx=5, pady=5)

if __name__ == "__main__":
    root = ctk.CTk()
    quiz = Quiz.from_sql(1)
    student = student.from_sql('2023BCY0001')
    StudentQuizReview(root, student, quiz).mainloop()
    root.mainloop()