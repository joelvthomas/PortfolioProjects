from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from data_base_connect import EventDatabase

class Singelton_AddEventsScreen:
    __instance = None

    def __new__(cls, root,enrollment_ID,user_name):
        if cls.__instance is None:
            cls.__instance = super(Singelton_AddEventsScreen, cls).__new__(cls)
            cls.__instance.create_widget(root,enrollment_ID,user_name)
        return cls.__instance

    def create_widget(self, root, enrollment_ID, user_name):
        self.add_events_window = Toplevel(root)
        self.add_events_window.title("Add Event")
        self.add_events_window.geometry("600x500")  # Increased height for new fields
        self.add_events_window.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('DEVELOPMENT/studentify.jpg'))
        self.bgimage_label = Label(self.add_events_window, image=self.bgimage)
        self.bgimage_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Location
        self.location_label = Label(self.add_events_window, text='Location', font=("times new roman", 15), bg="white")
        self.location_label.place(x=50, y=50)
        self.location_entry = Entry(self.add_events_window, font=("times new roman", 15))
        self.location_entry.place(x=200, y=50, width=300)

        # Event Name
        self.event_name_label = Label(self.add_events_window, text='Event Name', font=("times new roman", 15), bg="white")
        self.event_name_label.place(x=50, y=100)
        self.event_name_entry = Entry(self.add_events_window, font=("times new roman", 15))
        self.event_name_entry.place(x=200, y=100, width=300)

        # Date (Day, Month, Year)
        self.date_label = Label(self.add_events_window, text='Date', font=("times new roman", 15), bg="white")
        self.date_label.place(x=50, y=150)

        self.day_var = StringVar()
        self.month_var = StringVar()
        self.year_var = StringVar()

        # Populate dropdowns with relevant data
        current_year = datetime.now().year
        self.day_options = [str(day).zfill(2) for day in range(1, 32)]
        self.month_options = [str(month).zfill(2) for month in range(1, 13)]
        self.year_options = [str(year) for year in range(current_year, current_year + 5)]

        self.day_menu = OptionMenu(self.add_events_window, self.day_var, *self.day_options)
        self.day_menu.place(x=200, y=150, width=80)
        self.day_var.set(self.day_options[0])

        self.month_menu = OptionMenu(self.add_events_window, self.month_var, *self.month_options)
        self.month_menu.place(x=300, y=150, width=80)
        self.month_var.set(self.month_options[0])

        self.year_menu = OptionMenu(self.add_events_window, self.year_var, *self.year_options)
        self.year_menu.place(x=400, y=150, width=80)
        self.year_var.set(self.year_options[0])

        # Time
        self.time_label = Label(self.add_events_window, text='Time (HH:MM)', font=("times new roman", 15), bg="white")
        self.time_label.place(x=50, y=200)
        self.time_entry = Entry(self.add_events_window, font=("times new roman", 15))
        self.time_entry.place(x=200, y=200, width=300)

        # About (Larger Text Area)
        self.about_label = Label(self.add_events_window, text='About', font=("times new roman", 15), bg="white")
        self.about_label.place(x=50, y=250)
        self.about_entry = Text(self.add_events_window, height=5, font=("times new roman", 15))
        self.about_entry.place(x=200, y=250, width=300)

        # Submit Button
        # Use a lambda to pass arguments to the submit_event method
        self.submit_btn = Button(self.add_events_window, text="Submit", font=("times new roman", 15), bg="lightblue", bd=2, 
                                command=lambda: self.submit_event(enrollment_ID, user_name))
        self.submit_btn.place(x=250, y=420, width=100)

        # Handle window close to reset instance
        self.add_events_window.protocol("WM_DELETE_WINDOW", self.on_close)

    
    

    def submit_event(self,enrollment_ID,user_name):
        location = self.location_entry.get()
        event_name = self.event_name_entry.get()
        date = f"{self.day_var.get()}-{self.month_var.get()}-{self.year_var.get()}"
        time = self.time_entry.get()
        about = self.about_entry.get("1.0", END).strip()
        host = user_name 
        host_id = enrollment_ID

        if not location or not event_name or not about or not time:
            messagebox.showerror("Error", "All fields are required.")
            self.on_close()
        else:
            try:
                # Convert the date and time to datetime object for validation
                datetime.strptime(f"{self.year_var.get()}-{self.month_var.get()}-{self.day_var.get()} {time}", "%Y-%m-%d %H:%M")
                # Save event data to database
                EventDatabase.add_event(location,event_name,date,time,about,host,host_id)
                # Implement event submission logic here
                messagebox.showinfo("Success", "Event added successfully.")
                self.on_close()
                
            except ValueError:
                messagebox.showerror("Error", "Invalid date or time format.")
                self.on_close()

    def on_close(self):
        """ Reset instance and close the window """
        
        Singelton_AddEventsScreen.__instance = None
        self.add_events_window.destroy()
