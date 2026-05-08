from tkinter import *
from tkinter import messagebox
from data_base_connect import EventDatabase, NotificationDatabase


class Singleton_ViewEvent:
    __instance = None

    def __new__(cls, root, current_user):
        if cls.__instance is None:
            cls.__instance = super(Singleton_ViewEvent, cls).__new__(cls)
            cls.__instance.create_widget(root, current_user)
        return cls.__instance

    def create_widget(self, root, current_user):
        self.view_events_window = Toplevel(root)
        self.view_events_window.title("View Events")
        self.view_events_window.geometry("800x600")
        self.view_events_window.resizable(False, False)
        
        self.current_user = current_user

        self.events_listbox = Listbox(self.view_events_window, font=("times new roman", 15))
        self.events_listbox.place(x=50, y=50, width=700, height=400)
        self.events_listbox.bind("<Double-Button-1>", self.show_event_details)

        self.load_events()

        # Handle window close to reset instance
        self.view_events_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_events(self):
        events = EventDatabase.get_events()
        for event in events:
            event_id, location, event_name, date, time, about, host, host_id = event
            self.events_listbox.insert(END, f"{event_name}")

    def show_event_details(self, event):
        selected_index = self.events_listbox.curselection()
        if selected_index:
            event_name = self.events_listbox.get(selected_index)
            events = EventDatabase.get_events()
            for event in events:
                event_id, location, event_name_db, date, time, about, host,host_id = event
                if event_name == event_name_db:
                    self.show_event_popup(event_id, location, event_name_db, date, time, about, host, host_id)

    def show_event_popup(self, event_id, location, event_name, date, time, about, host, host_id):
        top = Toplevel(self.view_events_window)
        top.title(event_name)
        top.geometry("400x400")
        
        Label(top, text=f"Event: {event_name}", font=("times new roman", 15)).pack()
        Label(top, text=f"Location: {location}", font=("times new roman", 15)).pack()
        Label(top, text=f"Date: {date}", font=("times new roman", 15)).pack()
        Label(top, text=f"Time: {time}", font=("times new roman", 15)).pack()
        Label(top, text=f"About: {about}", font=("times new roman", 15)).pack()
        

        # Get the host details
        event_host = host
        Label(top, text=f"Host: {event_host}", font=("times new roman", 15)).pack()

        # RSVP Dropdown
        self.rsvp_var = StringVar(value="Select RSVP")
        rsvp_menu = OptionMenu(top, self.rsvp_var, "Yes", "No", "Maybe")
        rsvp_menu.pack()

        Button(top, text="Submit RSVP", command=lambda: self.submit_rsvp(event_id,event_name)).pack()

        rsvp_people = EventDatabase.get_event_rsvps(event_id)
        print(len(rsvp_people))
        if rsvp_people:

            Label(top, text="People response to event:", font=("times new roman", 15)).pack()
            for person in rsvp_people:
                
                    Label(top, text=person, font=("times new roman", 15)).pack()

    

    def submit_rsvp(self, event_id,event_name):
        rsvp_option = self.rsvp_var.get()
        if rsvp_option == "Select RSVP":
            messagebox.showerror("Error", "Please select an RSVP option.")
            return
        # Add the RSVP to the database
        EventDatabase.add_rsvp(event_id, self.current_user,rsvp_option)
        
        # Notify the host with the RSVP option
        
        host_id=EventDatabase.get_event_host(event_id)
        NotificationDatabase.add_notification(host_id, f"The student {self.current_user} said {rsvp_option} for your event {event_name}")
        self.on_close()
        messagebox.showinfo("RSVP", f"You have RSVPed with option: {rsvp_option}.")

    def on_close(self):
        """ Reset instance and close the window """
        Singleton_ViewEvent.__instance = None
        self.view_events_window.destroy()


   