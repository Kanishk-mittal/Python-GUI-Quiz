import customtkinter as ctk
from Models.Teacher import Teacher
from Models.Quiz import Quiz
from Models.Question import Question
from UI.Components.Add_mcq_question import AddMCqQuestion
from UI.Components.Add_short_answer_question import AddShortQuestion
from UI.Components.Add_long_answer_question import AddLongQuestion

class AddQuestion(ctk.CTkToplevel):
    def __init__(self, teacher, **kwargs):
        super().__init__(**kwargs)
        self.teacher = teacher
        self.title("Add Quiz")
        self.quiz_id=Quiz.get_next_id() 

        # Top frame
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=10, padx=10, fill="x")

        # Left frame for quiz name
        self.left_frame = ctk.CTkFrame(self.top_frame)
        self.left_frame.pack(side="left", padx=10)

        self.quiz_name_label = ctk.CTkLabel(self.left_frame, text="Quiz Name:", font=("Arial", 16))
        self.quiz_name_label.pack(pady=5)
        self.quiz_name_entry = ctk.CTkEntry(self.left_frame, width=200, font=("Arial", 16))
        self.quiz_name_entry.pack(pady=5)

        # Right frame for other inputs
        self.right_frame = ctk.CTkFrame(self.top_frame)
        self.right_frame.pack(side="right", padx=10,ipadx=20)

        self.no_of_attempts_label = ctk.CTkLabel(self.right_frame, text="No of Attempts:")
        self.no_of_attempts_label.pack(pady=5)
        self.no_of_attempts_entry = ctk.CTkEntry(self.right_frame)
        self.no_of_attempts_entry.pack(pady=5)

        self.assigned_to_batch_label = ctk.CTkLabel(self.right_frame, text="Assigned to Batch:")
        self.assigned_to_batch_label.pack(pady=5)
        self.assigned_to_batch_entry = ctk.CTkEntry(self.right_frame)
        self.assigned_to_batch_entry.pack(pady=5)

        self.assigned_to_semester_label = ctk.CTkLabel(self.right_frame, text="Assigned to Semester:")
        self.assigned_to_semester_label.pack(pady=5)
        self.assigned_to_semester_entry = ctk.CTkEntry(self.right_frame)
        self.assigned_to_semester_entry.pack(pady=5)

        # Frame for questions
        self.questions_frame = ctk.CTkFrame(self)
        self.questions_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.questions_frame)
        self.scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Buttons to add questions
        self.buttons_frame = ctk.CTkFrame(self.questions_frame)
        self.buttons_frame.pack(pady=10, padx=10, fill="x")

        self.add_mcq_button = ctk.CTkButton(self.buttons_frame, text="Add MCQ Question", command=self.add_mcq_question)
        self.add_mcq_button.pack(side="left", padx=5)

        self.add_long_answer_button = ctk.CTkButton(self.buttons_frame, text="Add Long Answer Question", command=self.add_long_answer_question)
        self.add_long_answer_button.pack(side="left", padx=5)

        self.add_short_answer_button = ctk.CTkButton(self.buttons_frame, text="Add Short Answer Question", command=self.add_short_answer_question)
        self.add_short_answer_button.pack(side="left", padx=5)

        # Center the buttons frame
        self.buttons_frame.pack_configure(anchor="center")

        # Finish button
        self.finish_button = ctk.CTkButton(self, text="Finish", command=self.finish)
        self.finish_button.pack(pady=10)

    def add_mcq_question(self):
        mcq_question = AddMCqQuestion(self.scrollable_frame, quiz_id=self.quiz_id)
        mcq_question.pack(pady=5, fill="x")

    def add_long_answer_question(self):
        long_answer_question = AddLongQuestion(quiz_id=self.quiz_id,master=self.scrollable_frame)
        long_answer_question.pack(pady=5, fill="x")

    def add_short_answer_question(self):
        short_answer_question = AddShortQuestion(quiz_id=self.quiz_id,master=self.scrollable_frame)
        short_answer_question.pack(pady=5, fill="x")

    def finish(self):
        quiz_name = self.quiz_name_entry.get()
        no_of_attempts = self.no_of_attempts_entry.get()
        assigned_to_batch = self.assigned_to_batch_entry.get()
        assigned_to_semester = self.assigned_to_semester_entry.get()

        questions = []
        for widget in self.scrollable_frame.winfo_children():
            if isinstance(widget, AddMCqQuestion) or isinstance(widget, AddLongQuestion) or isinstance(widget, AddShortQuestion):
                questions.append(widget.get_question())

        quiz = Quiz(
            made_by=self.teacher.name,
            assigned_to_batch=assigned_to_batch,
            assigned_to_semester=assigned_to_semester,
            no_of_questions=len(questions),
            total_marks=None,  # This will be calculated
            questions=questions,
            last_date=None,  # This should be set appropriately
            number_of_attempts=int(no_of_attempts),
            quiz_id=None,  # This should be set appropriately
            name=quiz_name
        )

        print(quiz)
        return quiz

if __name__ == "__main__":
    Teacher = Teacher.get_teacher_by_username("johnson")
    root = ctk.CTk()
    app = AddQuestion(teacher=Teacher, master=root)
    app.mainloop()
    root.destroy()
    