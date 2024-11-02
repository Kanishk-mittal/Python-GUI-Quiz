import customtkinter as ctk
class McqQuestion(ctk.CTkFrame):
    """
    A custom frame widget for displaying MCQ question information.
    Attributes:
        question (str): The question to be displayed.
        options (list): an array options to be displayed.
    Methods:
        create_widgets():
            Creates and arranges the widgets within the frame.
        get_answer():
            Method for getting the selected answer i.e it will return the value of the selected option.
    """
    def __init__(self, master=None, question=None, options=None):
        super().__init__(master)
        self.question = question
        self.options = options
        self.create_widgets()
        
    def create_widgets(self):
        # First part: Question
        self.question_label = ctk.CTkLabel(self, text=self.question)
        self.question_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Second part: Options
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.grid(row=1, column=0, padx=10, pady=10)
        
        self.selected_option = ctk.IntVar()
        
        for index, option in enumerate(self.options):
            option_radio = ctk.CTkRadioButton(self.options_frame, text=option, variable=self.selected_option, value=index)
            option_radio.grid(row=index, column=0, padx=5, pady=5)
    
    def get_answer(self):
        return self.options[self.selected_option.get()]

if __name__ == '__main__':
    question = "What is the capital of India?"
    options = ["New Delhi", "Mumbai", "Kolkata", "Chennai"]
    root=ctk.CTk()
    mcq = McqQuestion(root, question, options)
    mcq.pack(padx=10, pady=10)
    ctk.CTkButton(root, text="Get Answer", command=lambda: print(mcq.get_answer())).pack(padx=10, pady=10)
    root.mainloop()