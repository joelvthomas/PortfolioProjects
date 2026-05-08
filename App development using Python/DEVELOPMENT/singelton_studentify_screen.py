from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os, sys
from singelton_addeventsscreen import Singelton_AddEventsScreen
from singelton_inquiryscreen import Singelton_InquiryScreen
from singelton_forum_post import SingletonForumPost
from singleton_view_event import Singleton_ViewEvent
from singelton_view_inquiries_screen import Singleton_ViewInquiriesScreen
from singleton_shownotification import Singleton_ShowNotification

class Singelton_Studentify_Screen:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singelton_Studentify_Screen, cls).__new__(cls)
            cls.__instance.create_widget()
        return cls.__instance

    def create_widget(self):
        self.studentify_screen = Tk()
        self.studentify_screen.title("Studentify")
        self.studentify_screen.geometry("1200x750")
        self.studentify_screen.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('DEVELOPMENT/studentify.jpg'))
        self.bgimage_label = Label(self.studentify_screen, image=self.bgimage)
        self.bgimage_label.place(x=0, y=0, relwidth=1, relheight=1)

        # User label
        self.user_label = Label(self.studentify_screen, font=("times new roman", 20), bg="lightgray")
        self.user_label.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Configure grid layout for responsiveness
        self.studentify_screen.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.studentify_screen.grid_rowconfigure((0,1, 2), weight=1)

        # Buttons
        self.add_events_btn = Button(self.studentify_screen, text="Add Events", font=("times new roman", 15), command=self.open_add_events_screen)
        self.add_events_btn.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.view_events_btn = Button(self.studentify_screen, text="View Events", font=("times new roman", 15), command=self.view_events)
        self.view_events_btn.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.forum_post_btn = Button(self.studentify_screen, text="Forum Post", font=("times new roman", 15), command=self.forum_post)
        self.forum_post_btn.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.inquiry_btn = Button(self.studentify_screen, text="Inquiry", font=("times new roman", 15), command=self.inquiry)
        self.inquiry_btn.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.view_inquiries_btn = Button(self.studentify_screen, text="View Inquiries", font=("times new roman", 15), command=self.view_inquiries)
        self.view_inquiries_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.notification_btn = Button(self.studentify_screen, text="Notification", font=("times new roman", 15), command=self.notification)
        self.notification_btn.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

        self.logout_btn = Button(self.studentify_screen, text="Logout", font=("times new roman", 15), command=self.logout)
        self.logout_btn.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    def set_user_label(self, username, account_type,enrollment_id):
        self.user_label.configure(text=f"Welcome {username}!\nAccount type: {account_type}")
        self.user_name = username
        self.account_type = account_type
        self.enrollment_id=enrollment_id

    def open_add_events_screen(self):
        Singelton_AddEventsScreen(self.studentify_screen, self.enrollment_id, self.user_name)
    def view_events(self):
        Singleton_ViewEvent(self.studentify_screen, self.user_name)

    def forum_post(self):
        SingletonForumPost(self.studentify_screen,self.enrollment_id).pass_name(self.user_name)

    def inquiry(self):
        Singelton_InquiryScreen(self.studentify_screen,self.enrollment_id)

    def view_inquiries(self):
        if self.account_type == "Student Representative":
            Singleton_ViewInquiriesScreen(self.studentify_screen)
        else:
            messagebox.showwarning("Access Denied", "You are not authorised to access this.")

    def notification(self):
        Singleton_ShowNotification(self.studentify_screen,self.enrollment_id)

    def logout(self):
        os.execv(sys.executable, [os.path.basename(sys.executable)] + sys.argv)

"""
if __name__ == "__main__":
    root = Tk()
    # Simulate a user login with their enrollment ID
    #user_enrollment_id = "as"  # Replace with the actual user's enrollment ID after login
    Singelton_Studentify_Screen().set_user_label("akhil","Student","1234")
    root.mainloop()
    """