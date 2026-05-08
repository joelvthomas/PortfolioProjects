from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from data_base_connect import InquiryDatabase

class Singelton_InquiryScreen:
    __instance = None

    def __new__(cls, root,enrollment_id):
        if cls.__instance is None:
            cls.__instance = super(Singelton_InquiryScreen, cls).__new__(cls)
            cls.__instance.create_widget(root,enrollment_id)
        return cls.__instance

    def create_widget(self, root,enrollment_id):
        self.inquiry_window = Toplevel(root)
        self.inquiry_window.title("Inquiry Form")
        self.inquiry_window.geometry("600x600")
        self.inquiry_window.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('DEVELOPMENT/studentify.jpg'))
        self.bgimage_label = Label(self.inquiry_window, image=self.bgimage)
        self.bgimage_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Name
        self.name_label = Label(self.inquiry_window, text='Name', font=("times new roman", 15), bg="white")
        self.name_label.place(x=50, y=50)
        self.name_entry = Entry(self.inquiry_window, font=("times new roman", 15))
        self.name_entry.place(x=250, y=50, width=300)

        # Enrollment ID
        self.enrollment_label = Label(self.inquiry_window, text='Enrollment ID', font=("times new roman", 15), bg="white")
        self.enrollment_label.place(x=50, y=100)
        self.enrollment_entry = Entry(self.inquiry_window, font=("times new roman", 15))
        self.enrollment_entry.place(x=250, y=100, width=300)
        # Set default value for the entry
        self.enrollment_entry.insert(0, enrollment_id)

        # Email
        self.email_label = Label(self.inquiry_window, text='Email', font=("times new roman", 15), bg="white")
        self.email_label.place(x=50, y=150)
        self.email_entry = Entry(self.inquiry_window, font=("times new roman", 15))
        self.email_entry.place(x=250, y=150, width=300)

        # Department (Dropdown)
        self.department_label = Label(self.inquiry_window, text='Department', font=("times new roman", 15), bg="white")
        self.department_label.place(x=50, y=200)
        self.department_var = StringVar()
        self.department_options = [
            "Technology and Bionics", "Life Sciences", 
            "Society and Economics", "Communication and Environment"
        ]
        self.department_menu = OptionMenu(self.inquiry_window, self.department_var, *self.department_options)
        self.department_menu.place(x=250, y=200, width=300)
        self.department_var.set(self.department_options[0])  # Set default value

        # Type of Inquiry (Dropdown)
        self.inquiry_type_label = Label(self.inquiry_window, text='Type of Inquiry', font=("times new roman", 15), bg="white")
        self.inquiry_type_label.place(x=50, y=250)
        self.inquiry_type_var = StringVar()
        self.inquiry_type_options = [
            "Examination", "Re-registration", "Studies",
            "Transcript and documents", "Workshops",
            "Co-curricular activities", "Sports"
        ]
        self.inquiry_type_menu = OptionMenu(self.inquiry_window, self.inquiry_type_var, *self.inquiry_type_options)
        self.inquiry_type_menu.place(x=250, y=250, width=300)
        self.inquiry_type_var.set(self.inquiry_type_options[0])  # Set default value

        # Subject
        self.subject_label = Label(self.inquiry_window, text='Subject', font=("times new roman", 15), bg="white")
        self.subject_label.place(x=50, y=300)
        self.subject_entry = Entry(self.inquiry_window, font=("times new roman", 15))
        self.subject_entry.place(x=250, y=300, width=300)

        # Details (Larger Text Area)
        self.details_label = Label(self.inquiry_window, text='Details', font=("times new roman", 15), bg="white")
        self.details_label.place(x=50, y=350)
        self.details_entry = Text(self.inquiry_window, height=5, font=("times new roman", 15))
        self.details_entry.place(x=250, y=350, width=300)

        # Submit Button
        self.submit_btn = Button(self.inquiry_window, text="Submit", font=("times new roman", 15), bg="lightblue", bd=2, command=self.submit_inquiry)
        self.submit_btn.place(x=250, y=500, width=100)

        # Handle window close to reset instance
        self.inquiry_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def submit_inquiry(self):
        name = self.name_entry.get()
        enrollment_id = self.enrollment_entry.get()
        email = self.email_entry.get()
        department = self.department_var.get()
        inquiry_type = self.inquiry_type_var.get()
        subject = self.subject_entry.get()
        details = self.details_entry.get("1.0", END).strip()
        
        if not name or not enrollment_id or not email or not subject or not details:
            messagebox.showerror("Error", "All fields are required.")
            self.on_close()
        else:
            try:
                # Save inquiry data to the database
                InquiryDatabase.add_inquiry(name, enrollment_id, email, department, inquiry_type, subject, details)
                # Implement inquiry submission logic here
                messagebox.showinfo("Success", "Inquiry submitted successfully.")
                self.on_close()
                
                
            except Exception as e:
                print (e)
                messagebox.showerror("Error",f"An error occurred: {e}")

    def on_close(self):
        """ Reset instance and close the window """
        
        Singelton_InquiryScreen.__instance = None
        self.inquiry_window.destroy()
