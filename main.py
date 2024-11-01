import customtkinter as ctk
from UI.Login import LoginForm
import mysql.connector as msc
import os
import dotenv
from Database.Creator import create

class App:
    def __init__(self):
        self.u_name = None
        self.app = ctk.CTk()
        self.app.withdraw()
        LoginForm(self.app, self.on_login)

    def on_login(self, username):
        print("Logged in successfully")
        self.u_name = username
        print(f"Username: {self.u_name}")

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    dotenv.load_dotenv()
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    conn=msc.connect(host="localhost",user="root",password=SQL_PASSWORD)
    cursor=conn.cursor()
    # check if the database exists
    cursor.execute("SHOW DATABASES LIKE 'quiz_system'")
    if not cursor.fetchone():
        create()
    conn.commit()
    cursor.close()
    conn.close()
    app_instance = App()
    app_instance.run()