import customtkinter as ctk
from Models.Quiz import Quiz
from Models.Teacher import Teacher
from tkinter.messagebox import askokcancel

class TeacherQuizCard(ctk.CTkFrame):
    """
    A custom frame widget for displaying quiz information and actions for a student.
    Attributes:
        quiz (Quiz): The quiz object containing details about the quiz.
        student_id (int): The ID of the student.
    Methods:
        create_widgets():
            Creates and arranges the widgets within the frame.
        review_quiz():
            Placeholder method for reviewing the quiz.
        attempt_quiz():
            Placeholder method for attempting the quiz.
    """
    def __init__(self, master=None, quiz=None, Teacher=None):
        super().__init__(master)
        self.quiz = quiz
        self.Teacher = Teacher
        self.create_widgets()

    def create_widgets(self):
        # First part: Quiz name
        self.quiz_name_label = ctk.CTkLabel(self, text=self.quiz.name)
        self.quiz_name_label.pack(side="left", padx=10, pady=10)

        # Second part: Quiz details
        self.details_frame = ctk.CTkFrame(self)
        self.details_frame.pack(side="left", padx=100, pady=10)

        self.total_marks_label = ctk.CTkLabel(self.details_frame, text=f"Total Marks: {self.quiz.total_marks}")
        self.total_marks_label.pack(padx=5, pady=5)

        self.no_of_questions_label = ctk.CTkLabel(self.details_frame, text=f"Questions: {self.quiz.no_of_questions}")
        self.no_of_questions_label.pack(padx=5, pady=5)

        # Third part: Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(side="right", padx=10, pady=10)

        self.review_button = ctk.CTkButton(self.buttons_frame, text="Remove", command=self.remove_quiz)
        self.review_button.pack(side="left", padx=5, pady=5)

        self.attempt_button = ctk.CTkButton(self.buttons_frame, text="Rename", command=self.rename)
        self.attempt_button.pack(side="left", padx=5, pady=5)

        self.attempt_button = ctk.CTkButton(self.buttons_frame, text="Get report", command=self.show_report)
        self.attempt_button.pack(side="left", padx=5, pady=5)

    def remove_quiz(self):
        if askokcancel("Remove quiz", "Are you sure you want to remove this quiz?"):
            self.Teacher.remove_quiz(self.quiz)
            self.destroy()

    def rename(self):
        new_name = ctk.CTkInputDialog(title="Rename quiz", text="Enter new name for the quiz").get_input()
        if new_name:
            self.quiz.name = new_name
            self.quiz.update_name(new_name)
            self.quiz_name_label.configure(text=new_name)
    
    def show_report(self):
        #TODO: Create a window to show the report
        print("Send report")

if __name__ == "__main__":
    Teacher = Teacher.get_teacher_by_username("johnson")
    quiz = Quiz.from_sql(1)
    root = ctk.CTk()
    app = TeacherQuizCard(Teacher=Teacher, quiz=quiz, master=root)
    app.pack(expand=True, fill='both')
    root.mainloop()