import customtkinter as ctk

class ShortAnswerQuestion(ctk.CTkFrame):
    """
    A custom frame widget for displaying short answer question information.
    Attributes:
        question (str): The question to be displayed.
        answer (str): The correct answer to the question.
    Methods:
        create_widgets():
            Creates and arranges the widgets within the frame.
        get_answer():
            Method for getting the answer entered by the user.
    """
    def __init__(self, master=None, question=None, answer=None):
        super().__init__(master)
        self.question = question
        self.answer = answer
        self.create_widgets()
        
    def create_widgets(self):
        # First part: Question
        self.question_label = ctk.CTkLabel(self, text=self.question)
        self.question_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Second part: Answer Entry
        self.answer_entry = ctk.CTkEntry(self)
        self.answer_entry.grid(row=1, column=0, padx=10, pady=10)
    
    def get_answer(self):
        return self.answer_entry.get()

if __name__ == '__main__':
    question = "What is the capital of India?"
    answer = "New Delhi"
    root=ctk.CTk()
    short_answer = ShortAnswerQuestion(root, question, answer)
    short_answer.pack(padx=10, pady=10)
    ctk.CTkButton(root, text="Get Answer", command=lambda: print(short_answer.get_answer())).pack(padx=10, pady=10)
    root.mainloop()