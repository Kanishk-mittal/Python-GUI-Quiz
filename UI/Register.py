import customtkinter as ctk

class Register(ctk.CTkToplevel):
    def __init__(self, master=None,register_student=None,is_student=None,register_teacher=None):
        super().__init__(master)
        self.title('Register')
        self.geometry("400x400")  
        self.resizable(False, False)
        self.register_student = register_student
        self.register_teacher = register_teacher
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

        self.password_label = ctk.CTkLabel(self, text='Password', font=('Arial', 14), )
        self.password_label.pack(pady=5)
        self.password = ctk.CTkEntry(self, show='*', width=200)
        self.password.pack(pady=5)

        self.register = ctk.CTkButton(self, text='Register', command=self.register_teacher, width=100)
        self.register.pack(pady=20)

if __name__ == '__main__':
    def register_student():
        print('Register Student')
    def register_teacher():
        print('Register Teacher')
    root = ctk.CTk()
    register = Register(root,register_student,False,register_teacher)
    # register = Register(root,register_student,True,register_teacher)
    root.mainloop()