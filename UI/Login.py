import customtkinter as ctk
class Login(ctk.CTkToplevel):
    """
    A custom login window class that inherits from ctk.CTkToplevel.
    Attributes:
        login_action (callable): A function to be called when the login button is pressed.
        register_action (callable): A function to be called when the register button is pressed.
    Methods:
        __init__(master=None, login_action=None, register_action=None):
            Initializes the login window with the given master and actions.
        create_widgets():
            Creates and packs the widgets for the login window.
    """
    def __init__(self, master=None,login_action=None,register_action=None):
        """
        Initializes the Login window.

        Args:
            master (Tk, optional): The parent widget. Defaults to None.
            login_action (callable, optional): The function to call when the login button is pressed. Defaults to None.
            register_action (callable, optional): The function to call when the register button is pressed. Defaults to None.
        """
        super().__init__(master)
        self.title('Login')
        self.geometry("400x400")  # Set the size of the window
        self.resizable(False, False)
        self.login_action = login_action
        self.register_action = register_action
        self.create_widgets()

    def create_widgets(self):
        """
        Create and pack the widgets for the login interface.
        This method initializes and arranges the following widgets:
        - A label displaying 'Login' with a specified font and text color.
        - A label for the 'Username' field with a specified font and text color.
        - An entry widget for the user to input their username.
        - A label for the 'Password' field with a specified font and text color.
        - An entry widget for the user to input their password, with masked input.
        - A button labeled 'Login' that triggers the login_action method when clicked.
        - A button labeled 'Register' that triggers the register method when clicked.
        """
        self.label = ctk.CTkLabel(self, text='Login', font=('Arial', 20), )
        self.label.pack(pady=20)

        self.username_label = ctk.CTkLabel(self, text='Username', font=('Arial', 14), )
        self.username_label.pack(pady=5)
        self.username = ctk.CTkEntry(self, width=200)
        self.username.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text='Password', font=('Arial', 14), )
        self.password_label.pack(pady=5)
        self.password = ctk.CTkEntry(self, show='*', width=200)
        self.password.pack(pady=5)

        self.login = ctk.CTkButton(self, text='Login', command=self.login_action, width=100)
        self.login.pack(pady=20)

        self.register = ctk.CTkButton(self, text='Register', command=self.register_action, width=100)
        self.register.pack(pady=20)
    def get_values(self):
        """
        Returns the values entered in the username and password fields.

        Returns:
            tuple: A tuple containing the username and password entered by the user.
        """
        return self.username.get(), self.password.get()
    def clear(self):
        self.username.setvar("")
        self.password.setvar("")
if __name__ == '__main__':
    root = ctk.CTk()
    root.iconify()
    app = Login(master=root,login_action=login_action,register_action=register)
    root.mainloop()