from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from user import User
from data_base_connect import LoginDatabase

from singelton_register_screen import Singelton_Register_Screen
from singelton_studentify_screen import Singelton_Studentify_Screen

from GUI import IGui


class Singelton_Homescreen(IGui):
    __instance = None

    def __new__(cls):
        if (cls.__instance==None):
            cls.__instance = super(Singelton_Homescreen,cls).__new__(cls)
            cls.__instance.create_widget()
        return cls.__instance
    
    def create_widget(self):
        ## create tkinter object and set properties
        self.home_screen = Tk()
        self.home_screen.title("STUDENTIFY")
        self.home_screen.geometry("1200x750")
        self.home_screen.resizable(False, False)

        ## set backround ##
        self.bg_image = ImageTk.PhotoImage(Image.open('DEVELOPMENT/background.jpg'))
        self.bg_label = Label(self.home_screen, image=self.bg_image)
        self.bg_label.image = self.bg_image
        self.bg_label.pack()

        # Username label and entry
        self.enrollment_label = Label(self.home_screen, font=("times new roman", 20), text='Enrollment ID')
        self.enrollment_label.place(x=550, y=250, width=250, height=40)
        self.enrollment_id: str = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray")
        self.enrollment_id.place(x=800, y=250, width=250, height=40)
        
        # Password label and entry
        self.password_label = Label(self.home_screen, font=("times new roman", 20), text='Password')
        self.password_label.place(x=550, y=350, width=250, height=40)
        self.password:str = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray") 
        self.password.config(show='*')
        self.password.place(x=800, y=350, width=250, height=40)

        # Login button
        self.login_btn = Button(self.home_screen, text="Login", command=self.login, font=("times new roman", 15),
                           bg="lightblue", bd=2, width=12, height=2)
        self.login_btn.place(x=850, y=450)

        # Register button
        self.register_btn = Button(self.home_screen,command=self.register_here, text="Register Here", 
                              font=("times new roman", 15), bg="lightblue", bd=2, width=12, height=2)
        self.register_btn.place(x=850, y=550)


    def get_enrollment_id(self):
        return self.enrollment_id.get()

    def get_password(self):
        return self.password.get()

    def create_user(self):
        user = User(self.get_enrollment_id(), self.get_password())
        return user

    def check_empty_feilds(self):
        user=self.create_user()
        if not user.get_enrollment_id() or not user.get_userpassw():
            messagebox.showerror("Error","All feilds are required.")
            return True
        else:
            return False

    def check_valid_user(self):
        row = LoginDatabase.is_existing_user(self.create_user())
       
        if row is None:
            messagebox.showerror("Error", "Invalid enrollment id and password")
            return False
        else:
            return True

    def login(self):
        try:
            if not self.check_empty_feilds() and self.check_valid_user():
                
                row = LoginDatabase.is_existing_user(self.create_user())
                user_account_type = row[2]
                name = row[0]
                enrollment_id= row[1]
                Singelton_Homescreen().home_screen.destroy()
                Singelton_Studentify_Screen().set_user_label(name,user_account_type,enrollment_id)
                

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def register_here(self):
        Singelton_Homescreen().home_screen.destroy()
        Singelton_Register_Screen()
        
