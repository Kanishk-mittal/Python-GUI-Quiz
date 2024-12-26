from UI.Login import Login
from Database.Creator import create
import mysql.connector as msc
from dotenv import load_dotenv
import customtkinter as ctk
import os
import re
from Models.Student import student
from Models.Teacher import Teacher
from UI.Student_dashboard import StudentDashboard
from tkinter.messagebox import showerror
from UI.Teacher_Dashboard import TeacherDashboard
from UI.Register import Register
from tkinter.messagebox import askyesno

load_dotenv()

def check_student(username):
    pattern = r'^\d{4}[a-zA-Z]{3}\d{4}$'
    if re.match(pattern, username):
        return True
    else:
        return False

def login_action(window,root):
    values=window.get_values()
    username=values[0]
    password=values[1]
    if(check_student(username=username)):
        student_obj = student.verify(username,password)
        if(student_obj):
            window.destroy()
            StudentDashboard(master=root,student=student_obj)
        else:
            showerror("Login Failed","Please enter correct credentials to proceed")
            window.clear()
    else:
        teacher = Teacher.verify(username,password)
        if teacher:
            window.destroy()
            TeacherDashboard(Teacher=teacher,master=root)
        else:
            showerror("Login Failed","Please enter correct credentials to proceed")
            window.clear()

def register(window,root):
    window.destroy()
    if askyesno("Register","Are you a student?"):
        root = ctk.CTk()
        register = Register(root,is_student=True)
    else:
        root = ctk.CTk()
        register = Register(root,is_student=False)

def main():
    # first check weather the database quiz_system exist or not
    # if not then create the database
    conn=msc.connect(host="localhost",user="root",password=os.getenv("SQL_PASSWORD"))
    cursor=conn.cursor()
    cursor.execute("SHOW DATABASES LIKE 'quiz_system'")
    if not cursor.fetchone():
        create()
    conn.close()
    # now create a root app
    root=ctk.CTk()
    root.title("Quiz System")
    root.geometry("400x400")
    login_window=Login(master=root,login_action=lambda: login_action(login_window,root),register_action=lambda: register(login_window,root))
    login_window.mainloop()

if __name__ == "__main__":
    main()