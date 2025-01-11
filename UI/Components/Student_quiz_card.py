import customtkinter as ctk
from Models.Quiz import Quiz
from UI.Student_quiz_review import StudentQuizReview

class StudentQuizCard(ctk.CTkFrame):
    """
    A custom frame widget for displaying quiz information and actions for a student.
    Attributes:
        quiz (Quiz): The quiz object containing details about the quiz.
        student (int): The ID of the student.
    Methods:
        create_widgets():
            Creates and arranges the widgets within the frame.
        review_quiz():
            Placeholder method for reviewing the quiz.
        attempt_quiz():
            Placeholder method for attempting the quiz.
    """
    def __init__(self, master=None,quiz=None,student=None):
        super().__init__(master)
        self.quiz = quiz
        self.student = student
        self.create_widgets()
    def create_widgets(self):
        # First part: Quiz name
        self.quiz_name_label = ctk.CTkLabel(self, text=self.quiz.name)
        self.quiz_name_label.grid(row=0, column=0, padx=10, pady=10)

        # Second part: Quiz details
        self.details_frame = ctk.CTkFrame(self)
        self.details_frame.grid(row=0, column=1, padx=10, pady=10)

        self.total_marks_label = ctk.CTkLabel(self.details_frame, text=f"Total Marks: {self.quiz.total_marks}")
        self.total_marks_label.grid(row=0, column=0, padx=5, pady=5)

        self.no_of_questions_label = ctk.CTkLabel(self.details_frame, text=f"Questions: {self.quiz.no_of_questions}")
        self.no_of_questions_label.grid(row=1, column=0, padx=5, pady=5)

        # Third part: Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.grid(row=0, column=2, padx=10, pady=10)

        self.review_button = ctk.CTkButton(self.buttons_frame, text="Review", command=self.review_quiz)
        self.review_button.grid(row=0, column=0, padx=5, pady=5)

        self.attempt_button = ctk.CTkButton(self.buttons_frame, text=f"Attempt ({self.quiz.attempts_left(self.student.roll_no)} left)", command=self.attempt_quiz)
        self.attempt_button.grid(row=0, column=1, padx=5, pady=5)

    def review_quiz(self):
        StudentQuizReview(self.master, self.student, self.quiz).mainloop()

    def attempt_quiz(self):
    # Implement the attempt quiz functionality
        pass

if __name__ == '__main__':
    quiz = Quiz(
        made_by="Instructor Name",
        assigned_to_batch="Batch A",
        assigned_to_semester="Semester 1",
        no_of_questions=10,
        total_marks=100,
        questions=["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"],
        last_date="2023-12-31",
        number_of_attempts=3,
        quiz_id="quiz123",
        name="Sample Quiz"
    )
    root = ctk.CTk()
    for i in range(5):
        StudentQuizCard(root, quiz, f"student{i}").pack(pady=10)
    root.mainloop()