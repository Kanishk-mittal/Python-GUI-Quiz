import customtkinter as ctk

class LongAnswerQuestion(ctk.CTkFrame):
    """
    A custom frame widget for displaying long answer question information.
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
        
        # Second part: Answer Text Area
        self.answer_text = ctk.CTkTextbox(self, width=400, height=200)
        self.answer_text.grid(row=1, column=0, padx=10, pady=10)
    
    def get_answer(self):
        return (self.question.question_id, self.answer_text.get("1.0", "end-1c"))

if __name__ == '__main__':
    question = "Describe the process of photosynthesis."
    answer = "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll."
    root = ctk.CTk()
    long_answer = LongAnswerQuestion(root, question, answer)
    long_answer.pack(padx=10, pady=10)
    ctk.CTkButton(root, text="Get Answer", command=lambda: print(long_answer.get_answer())).pack(padx=10, pady=10)
    root.mainloop()