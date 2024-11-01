import customtkinter as ctk
from Components.Student_quiz_card import StudentQuizCard
from Models.Student import Student
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StudentDashboard(ctk.CTkToplevel):
    """
    A custom toplevel widget for displaying the student dashboard.
    Methods:
        create_widgets():
            Creates and arranges the widgets within the toplevel.
    """
    def __init__(self, student, master=None):
        super().__init__(master)
        self.student = student
        self.create_widgets()

    def create_widgets(self):
        # First part: Welcome message with name of student that we can get from the student object using student.name
        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome {self.student.name}")
        self.welcome_label.pack(padx=10, pady=10)
        
        # Adding Logout and Get Report buttons
        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.pack(padx=10, pady=5)
        
        self.get_report_button = ctk.CTkButton(self, text="Get Report", command=self.get_report)
        self.get_report_button.pack(padx=10, pady=5)
        
        # at the right side of the welcome message, we will display the pie chart which we will get using student.get_pie()
        canvas = FigureCanvasTkAgg(self.student.get_pie(), master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side="right")
        
        # Second part: Display mini report which we can get through student.mini_report() which will return a dictionary with keys as no_of_attempts, avg_percentage, avg_accuracy
        self.mini_report = self.student.mini_report()
        self.mini_report_label = ctk.CTkLabel(self, text=f"Number of attempts: {self.mini_report['no_of_attempts']}\nAverage percentage: {self.mini_report['avg_percentage']}\nAverage accuracy: {self.mini_report['avg_accuracy']}")
        self.mini_report_label.pack(padx=10, pady=10)
        
        # Third part: Display the list of quizzes that the student can attempt
        self.quiz_list_label = ctk.CTkLabel(self, text="Quizzes")
        self.quiz_list_label.pack(padx=10, pady=10)
        self.quiz_list = ctk.CTkFrame(self)
        self.quiz_list.pack(padx=10, pady=10)
        
        # We will create a StudentQuizCard for each quiz in the student.get_quizzes()
        for quiz in self.student.get_quizzes():
            quiz_card = StudentQuizCard(self.quiz_list, quiz)
            quiz_card.pack(padx=10, pady=10)
    
    def logout(self):
        # Implement the logout functionality here
        pass
    
    def get_report(self):
        # Implement the get report functionality here
        pass

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    student = Student()  # Assuming you have a way to create or get a Student object
    student_dashboard = StudentDashboard(student)
    student_dashboard.mainloop()
    root.destroy()