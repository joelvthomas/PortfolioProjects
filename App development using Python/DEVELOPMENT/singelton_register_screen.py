from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

from GUI import IGui
from user import NewUser
from data_base_connect import LoginDatabase
from singelton_studentify_screen import Singelton_Studentify_Screen






class Singelton_Register_Screen(IGui):
    __instance = None

    def __new__(cls):
        if (cls.__instance==None):
            cls.__instance = super(Singelton_Register_Screen,cls).__new__(cls)
            cls.__instance.create_widget()
        return cls.__instance
    

    def create_widget(self):
        ## create tkinter object and set properties
        self.register_screen = Tk()
        self.register_screen.title("Registration Window")
        self.register_screen.geometry("1200x750")
        self.register_screen.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('DEVELOPMENT/background.jpg'))
        self.bgimage_label = Label(self.register_screen,image=self.bgimage)
        self.bgimage_label.image = self.bgimage
        self.bgimage_label.pack()

        # Enrollment
        self.enrollment_id_label = Label(self.register_screen,font=("times new roman", 20), text='Enrollment ID')
        self.enrollment_id_label.place(x=550, y=150, width=250, height=40)
        self.enrollment_id = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.enrollment_id.place(x=800, y=150, width=250, height=40)

        #  Name
        self.name_label = Label(self.register_screen,font=("times new roman", 20), text='Full Name')
        self.name_label.place(x=550, y=200, width=250, height=40)
        self.name = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.name.place(x=800, y=200, width=250, height=40)

        # Account type in drop down
        self.account_type_label = Label(self.register_screen, font=("times new roman", 20), text='Account Type')
        self.account_type_label.place(x=550, y=250, width=250, height=40)
        # Create a Combobox widget instead of Entry
        self.account_type = ttk.Combobox(self.register_screen, font=("times new roman", 20), values=["Student", "Student Representative"], state="readonly")
        self.account_type.place(x=800, y=250, width=250, height=40)
        #set default as student
        self.account_type.set("Student")

        # Email
        self.email_label = Label(self.register_screen,font=("times new roman", 20), text='Email')
        self.email_label.place(x=550, y=300, width=250, height=40)
        self.email = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.email.place(x=800, y=300, width=250, height=40)

        # Password
        self.password_label = Label(self.register_screen,font=("times new roman", 20), text='Password')
        self.password_label.place(x=550, y=350, width=250, height=40)
        self.password = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.password.place(x=800, y=350, width=250, height=40)

        # Confirm Password
        self.conpassword_label = Label(self.register_screen,font=("times new roman", 20), text='Confirm Password')
        self.conpassword_label.place(x=550, y=400, width=250, height=40)
        self.conpassword = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.conpassword.place(x=800, y=400, width=250, height=40)

        # Register button
        self.register_btn = Button(self.register_screen,text="Register",command=self.register,
                                   font=("times new roman", 15), bg="lightblue", bd=2, width=12, height=2)
        self.register_btn.place(x=850, y=550)

    ## define getters
    def get_enrollment_id(self):
        return self.enrollment_id.get()
    def get_password(self):
        return self.password.get()
    def get_name(self):
        return self.name.get()
    def get_account_type(self):
        return self.account_type.get()
    def get_user_email(self):
        return self.email.get()
    def get_conpassword(self):
        return self.conpassword.get()

    ## create a new user from entry 
    def create_new_user(self):
       
        new_user = NewUser( 
            self.get_enrollment_id(),
            self.get_name(),
            self.get_account_type(),
            self.get_user_email(),
            self.get_password(),
            self.get_conpassword()
        )
        return new_user
    
    ## check empty fields
    def check_empty_fields(self):
        
        if any(value=="" for value in \
               self.create_new_user().get_user_data().values()):
            
            messagebox.showerror("Error", "All fields are required.")
            return True
        else:
            return False
    ## check matching password
    def password_matched(self):
        if self.create_new_user().get_userpassw() != \
            self.create_new_user().get_confirmed_passw():
            messagebox.showerror("Error", "Passwords don't match.")
            return False
        else:
            return True
        
    ## check for existing enrollment_id
    def enrollment_id_exists(self):
        current_user=  self.create_new_user()
        if LoginDatabase.is_existing_user(current_user):
            messagebox.showerror("Error", "User already exists. Please try another username.")
            return True
        else:
            return False


    ## register new user to database:
    def register(self):
        try:
            if not self.check_empty_fields() and self.password_matched() and not self.enrollment_id_exists():
                
                LoginDatabase.upload_data(self.create_new_user())
                messagebox.showinfo("OK","You are registered.")
                name = self.get_name()
                user_account_type = self.get_account_type()
                enrollment_id=self.get_enrollment_id()
                self.register_screen.destroy()
                Singelton_Studentify_Screen().set_user_label(name,user_account_type,enrollment_id)
                

        except Exception as e:
            messagebox.showerror("Error", str(e))