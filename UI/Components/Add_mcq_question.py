import customtkinter as ctk
from Models.Quiz import Quiz
from Models.Question import Question

class AddMCqQuestion(ctk.CTkFrame):
    def __init__(self, master, quiz_id, **kwargs):
        super().__init__(master, **kwargs)
        self.quiz_id = quiz_id
        self.option_count = 0

        # Text area for question
        self.question_label = ctk.CTkLabel(self, text="Enter the question:")
        self.question_label.pack(pady=5)
        self.question_text = ctk.CTkTextbox(self, width=400, height=100)
        self.question_text.pack(pady=10)

        # Input box for first option
        self.option_frame = ctk.CTkFrame(self)
        self.option_frame.pack(pady=10)
        self.options = []
        self.add_option_input()

        # Button to add new option
        self.add_option_button = ctk.CTkButton(self, text="Add Option", command=self.add_option_input)
        self.add_option_button.pack(pady=10)

        # Input for correct option
        self.correct_option_label = ctk.CTkLabel(self, text="Correct Option (a, b, c, ...):")
        self.correct_option_label.pack(pady=5)
        self.correct_option_input = ctk.CTkEntry(self)
        self.correct_option_input.pack(pady=5)

        # input to get marks
        self.marks_label = ctk.CTkLabel(self, text="Marks:")
        self.marks_label.pack(pady=5)
        self.marks_input = ctk.CTkEntry(self)
        self.marks_input.pack(pady=5)

    def add_option_input(self):
        self.option_count += 1
        option_label = ctk.CTkLabel(self.option_frame, text=f"Option {chr(96 + self.option_count)}:")
        option_label.pack(pady=5)
        option_input = ctk.CTkEntry(self.option_frame)
        option_input.pack(pady=5)
        self.options.append(option_input)
    def get_question(self):
        options = {}
        for option in self.options:
            options[chr(96 + self.options.index(option) + 1)] = option.get()
        
        q= Question(statement=self.question_text.get("1.0", "end-1c"), options=options, answer=self.correct_option_input.get(), quiz_id=self.quiz_id, marks=self.marks_input.get(),typ="MCQ")
        print(q)
        return q
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = AddMCqQuestion(root, 1)
    app.pack()
    root.mainloop()
    root.destroy()