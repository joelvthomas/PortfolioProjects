# singleton_shownotification.py

from tkinter import *
from data_base_connect import NotificationDatabase, LoginDatabase

class Singleton_ShowNotification:
    __instance = None

    def __new__(cls, root, enrollment_id):
        if cls.__instance is None:
            cls.__instance = super(Singleton_ShowNotification, cls).__new__(cls)
            cls.__instance.create_widget(root, enrollment_id)
        return cls.__instance

    def create_widget(self, root, enrollment_id):
        self.notification_window = Toplevel(root)
        self.notification_window.title("Notifications")
        self.notification_window.geometry("400x400")
        self.notification_window.resizable(False, False)

        # Notification Listbox
        self.notification_listbox = Listbox(self.notification_window, font=("times new roman", 12), width=50, height=20)
        self.notification_listbox.pack(pady=20)

        # Load Notifications
        self.load_notifications(enrollment_id)

        # Handle window close
        self.notification_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_notifications(self, enrollment_id):
        notifications = NotificationDatabase.get_user_notifications(enrollment_id)
        for notification in notifications:
            self.notification_listbox.insert(END, notification)
        # Mark notifications as read after displaying them
        NotificationDatabase.mark_as_read(enrollment_id)

    def on_close(self):
        Singleton_ShowNotification.__instance = None
        self.notification_window.destroy()