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
    def __init__(self, master=None, question=None):
        super().__init__(master)
        self.question = question
        self.create_widgets()
        
    def create_widgets(self):
        # First part: Question
        self.question_label = ctk.CTkLabel(self, text=self.question.question)
        self.question_label.pack(pady=10,expand=True, fill="both")
        
        # Second part: Options
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10,expand=True, fill="both",side="left")
        
        self.selected_option = ctk.StringVar()
        i=0
        for key,value in self.question.options.items():
            option_radio = ctk.CTkRadioButton(self.options_frame, text=value, variable=self.selected_option, value=key)
            option_radio.pack(pady=10)
            i+=1
    
    def get_answer(self):
        return self.question.options[self.selected_option.get()]
