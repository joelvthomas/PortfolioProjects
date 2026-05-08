from tkinter import *
from tkinter import messagebox
from data_base_connect import InquiryDatabase, NotificationDatabase, LoginDatabase

class Singleton_ViewInquiriesScreen:
    __instance = None

    def __new__(cls, root):
        if cls.__instance is None:
            cls.__instance = super(Singleton_ViewInquiriesScreen, cls).__new__(cls)
            cls.__instance.create_widget(root)
        return cls.__instance

    def create_widget(self, root):
        self.view_inquiries_window = Toplevel(root)
        self.view_inquiries_window.title("View Inquiries")
        self.view_inquiries_window.geometry("1200x750")
        self.view_inquiries_window.resizable(True, True)

        # Inquiries Listbox
        self.inquiries_listbox = Listbox(self.view_inquiries_window, font=("times new roman", 12), width=100, height=15)
        self.inquiries_listbox.place(x=50, y=50, width=400, height=600)
        self.inquiries_listbox.bind("<Double-Button-1>", self.show_inquiry_details)

        # Inquiry Details
        self.details_label = Label(self.view_inquiries_window, text="", font=("times new roman", 14), wraplength=750, anchor="w")
        self.details_label.place(x=500, y=50, width=650, height=400)

        # Reply Section
        self.reply_label = Label(self.view_inquiries_window, text="Reply:", font=("times new roman", 15))
        self.reply_label.place(x=500, y=460)

        self.reply_text = Text(self.view_inquiries_window, font=("times new roman", 15), height=8, width=60)
        self.reply_text.place(x=500, y=490)

        self.submit_reply_btn = Button(self.view_inquiries_window, text="Submit Reply", font=("times new roman", 15), command=self.submit_reply)
        self.submit_reply_btn.place(x=650, y=650)

        # Load Inquiries
        self.load_inquiries()

        # Handle window close
        self.view_inquiries_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_inquiries(self):
        inquiries = InquiryDatabase.get_inquiries()
        self.inquiries_listbox.delete(0, END)  # Clear any existing items
        for inquiry in inquiries:
            # Adjust the unpacking logic to match the number of columns in the database
            inquiry_id, name, enrollment_id, email, department, inquiry_type, subject, details, status = inquiry
            self.inquiries_listbox.insert(END, f"{subject} - {name}")

    def show_inquiry_details(self, event):
        selected_index = self.inquiries_listbox.curselection()
        if selected_index:
            subject_name = self.inquiries_listbox.get(selected_index)
            inquiries = InquiryDatabase.get_inquiries()
            for inquiry in inquiries:
                # Adjust the unpacking logic to match the number of columns in the database
                inquiry_id, name, enrollment_id, email, department, inquiry_type, subject, details, status = inquiry
                if f"{subject} - {name}" == subject_name:
                    self.details_label.config(text=f"From: {name} ({email})\nDepartment: {department}\nType: {inquiry_type}\nDetails: {details}")
                    self.current_inquiry_id = inquiry_id
                    self.current_inquirer_id = enrollment_id  # Track who asked the inquiry
                    break

    def submit_reply(self):
        reply_content = self.reply_text.get("1.0", END).strip()
        if reply_content:
            
            current_user = LoginDatabase.get_user_details(self.current_inquirer_id)
            print(f"current_user is {self.current_inquirer_id}")
            if current_user:
                       
                InquiryDatabase.add_reply(self.current_inquiry_id, current_user['enrollment_id'], reply_content)
                
                NotificationDatabase.add_notification(current_user['enrollment_id'], f"Your inquiry has been replied: {reply_content}")
                
                messagebox.showinfo("Success", "Reply submitted and notification sent successfully.")
                self.reply_text.delete("1.0", END)
                self.load_inquiries()

    def on_close(self):
        Singleton_ViewInquiriesScreen.__instance = None
        self.view_inquiries_window.destroy()
