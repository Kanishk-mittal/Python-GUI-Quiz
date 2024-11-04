import customtkinter as ctk
from Models.Teacher import Teacher  
from UI.Components.Teacher_quiz_card import TeacherQuizCard

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

        self._button = ctk.CTkButton(self._header_frame, text="Logout", command=self._logout)
        self._button.pack(side="right", padx=10)

        # srollable frame for quiz cards
        self._scrollable_frame = ctk.CTkScrollableFrame(self._frame)
        self._scrollable_frame.pack(fill="both", expand=True)

        for quiz in self.Teacher.quizzes:
            quiz_card = TeacherQuizCard(master=self._scrollable_frame, quiz=quiz, Teacher=self.Teacher)
            quiz_card.pack(fill="x", padx=10, pady=10,expand=True)
        
        # add a button to add a new quiz
        self._add_button = ctk.CTkButton(self._frame, text="Add Quiz", command=self._add_quiz)
        self._add_button.pack(side="bottom", pady=10)

    def _logout(self):
        self.destroy()
    def _add_quiz(self):
        print("Add quiz")

if __name__ == "__main__":
    Teacher=Teacher.get_teacher_by_username("johnson")
    root=ctk.CTk()
    app = TeacherDashboard(Teacher,master=root)
    app.mainloop()
    root.destroy()
