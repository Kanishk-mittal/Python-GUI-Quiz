import customtkinter as ctk
from Models.Teacher import Teacher
from Models.Student import student
from UI.Student_dashboard import StudentDashboard
from UI.Teacher_Dashboard import TeacherDashboard

class Register(ctk.CTkToplevel):
    def __init__(self, master=None,is_student=None):
        super().__init__(master)
        self.master=master
        self.title('Register')
        self.geometry("400x400")  
        if is_student:
            self.create_student_form()
        else:
            self.create_teacher_form()

    def create_student_form(self):
        self.label = ctk.CTkLabel(self, text='Register as Student', font=('Arial', 20), )
        self.label.pack(pady=20)

        self.roll_label = ctk.CTkLabel(self, text='Roll Number', font=('Arial', 14), )
        self.roll_label.pack(pady=5)
        self.roll = ctk.CTkEntry(self, width=200)
        self.roll.pack(pady=5)

        self.name_label = ctk.CTkLabel(self, text='Name', font=('Arial', 14), )
        self.name_label.pack(pady=5)
        self.name = ctk.CTkEntry(self, width=200)
        self.name.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text='Email', font=('Arial', 14), )
        self.email_label.pack(pady=5)
        self.email = ctk.CTkEntry(self, width=200)
        self.email.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text='Password', font=('Arial', 14), )
        self.password_label.pack(pady=5)
        self.password = ctk.CTkEntry(self, show='*', width=200)
        self.password.pack(pady=5)

        self.register = ctk.CTkButton(self, text='Register', command=self.register_student, width=100)
        self.register.pack(pady=20)
    
    def create_teacher_form(self):
        self.label = ctk.CTkLabel(self, text='Register as Teacher', font=('Arial', 20), )
        self.label.pack(pady=20)

        self.name_label = ctk.CTkLabel(self, text='Name', font=('Arial', 14), )
        self.name_label.pack(pady=5)
        self.name = ctk.CTkEntry(self, width=200)
        self.name.pack(pady=5)

        self.username_label = ctk.CTkLabel(self, text='Username', font=('Arial', 14), )
        self.username_label.pack(pady=5)
        self.username = ctk.CTkEntry(self, width=200)
        self.username.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text='Email', font=('Arial', 14), )
        self.email_label.pack(pady=5)
        self.email = ctk.CTkEntry(self, width=200)
        self.email.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text='Password', font=('Arial', 14), )
        self.password_label.pack(pady=5)
        self.password = ctk.CTkEntry(self, show='*', width=200)
        self.password.pack(pady=5)

        self.register = ctk.CTkButton(self, text='Register', command=self.register_teacher, width=100)
        self.register.pack(pady=20)
    def register_student(self):
        student_name = self.name.get()
        roll_number = self.roll.get()
        password = self.password.get()
        email = self.email.get()
        student_obj = student(name=student_name,roll_no=roll_number,password=password,email=email)
        student_obj.to_sql()
        self.destroy()
        StudentDashboard(master=self.master,student=student_obj)

    def register_teacher(self):
        teacher_name = self.name.get()
        username = self.username.get()
        password = self.password.get()
        email = self.email.get()
        teacher_obj = Teacher(name=teacher_name,username=username,password=password,email=email)
        teacher_obj.to_sql()
        self.destroy()
        TeacherDashboard(master=self.master,Teacher=teacher_obj)

if __name__ == '__main__':
    root = ctk.CTk()
    register = Register(root,register_student,False,register_teacher)
    # register = Register(root,register_student,True,register_teacher)
    root.mainloop()