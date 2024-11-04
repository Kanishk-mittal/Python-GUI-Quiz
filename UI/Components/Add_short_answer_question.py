import customtkinter as ctk
from Models.Quiz import Quiz
from Models.Question import Question

class AddShortQuestion(ctk.CTkFrame):
    def __init__(self, quiz_id, master=None,**kwargs):
        super().__init__(master, **kwargs)
        self.quiz_id = quiz_id
        
        self.question_label=ctk.CTkLabel(self,text="Enter the question:")
        self.question_label.pack(pady=5)
        self.question_text = ctk.CTkTextbox(self, width=400, height=100)
        self.question_text.pack(pady=10)

        self.marks_label = ctk.CTkLabel(self, text="Marks:")
        self.marks_label.pack(pady=5)

        self.marks_entry = ctk.CTkEntry(self)
        self.marks_entry.pack(pady=5)
        
        self.correct_answer_label = ctk.CTkLabel(self, text="Correct Answer:")
        self.correct_answer_label.pack(pady=5)
        
        self.correct_answer_entry = ctk.CTkEntry(self, width=400)
        self.correct_answer_entry.pack(pady=10)

    def get_question(self):
        q= Question(statement=self.question_text.get("1.0", "end-1c"), answer=self.correct_answer_entry.get(), quiz_id=self.quiz_id,typ="Short Answer",marks=self.marks_entry.get())
        print(q)
        return q
if __name__ == "__main__":
    root = ctk.CTk()
    app = AddShortQuestion(1,root)
    app.pack()
    root.mainloop()
    root.destroy()