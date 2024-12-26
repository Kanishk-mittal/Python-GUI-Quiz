import customtkinter as ctk
from Models.Teacher import Teacher  
from UI.Components.Teacher_quiz_card import TeacherQuizCard
from UI.Add_quiz import AddQuiz

class TeacherDashboard(ctk.CTkToplevel):
    def __init__(self,Teacher,master=None):
        ctk.CTkToplevel.__init__(self, master)
        self.Teacher=Teacher
        self.title("Teacher Dashboard")
        self.geometry("800x600")
        self._initUI()

    def _initUI(self):
        self._frame = ctk.CTkFrame(self)
        self._frame.pack(fill="both", expand=True)

        self._header_frame = ctk.CTkFrame(self._frame)
        self._header_frame.pack(fill="x", pady=10, padx=10,ipady=20)

        self._label = ctk.CTkLabel(self._header_frame, text=f"Welcome, {self.Teacher.name}", font=("Helvetica", 16, "bold"))
        self._label.pack(side="left", padx=10)

        self._button = ctk.CTkButton(self._header_frame, text="Exit", command=self._quit,fg_color="#E71C23")
        self._button.pack(side="right", padx=10)

        # srollable frame for quiz cards
        self._scrollable_frame = ctk.CTkScrollableFrame(self._frame)
        self._scrollable_frame.pack(fill="both", expand=True)

        for quiz in self.Teacher.quizzes:
            quiz_card = TeacherQuizCard(master=self._scrollable_frame, quiz=quiz, Teacher=self.Teacher)
            quiz_card.pack(fill="x", padx=10, pady=10,expand=True)
        
        if len(self.Teacher.quizzes) == 0:
            self._no_quiz_label = ctk.CTkLabel(self._scrollable_frame, text="You have no quizzes added yet", font=("Helvetica", 12))
            self._no_quiz_label.pack(pady=10)
        
        # add a button to add a new quiz
        self._add_button = ctk.CTkButton(self._frame, text="Add Quiz", command=self._add_quiz)
        self._add_button.pack(side="bottom", pady=10)

    def _quit(self):
        exit()

    def _add_quiz(self):
        self.add_quiz_window = AddQuiz(self.Teacher, master=self)
        self.add_quiz_window.grab_set()
        self.Teacher=Teacher.verify(self.Teacher.username,self.Teacher.password)
        for widget in self._scrollable_frame.winfo_children():
            widget.destroy()
        for quiz in self.Teacher.quizzes:
            quiz_card = TeacherQuizCard(master=self._scrollable_frame, quiz=quiz, Teacher=self.Teacher)
            quiz_card.pack(fill="x", padx=10, pady=10,expand=True)
        if len(self.Teacher.quizzes) == 0:
            self._no_quiz_label = ctk.CTkLabel(self._scrollable_frame, text="You have no quizzes added yet", font=("Helvetica", 12))
            self._no_quiz_label.pack(pady=10)

if __name__ == "__main__":
    Teacher=Teacher.get_teacher_by_username("johnson")
    root=ctk.CTk()
    app = TeacherDashboard(Teacher,master=root)
    app.mainloop()
    root.destroy()
