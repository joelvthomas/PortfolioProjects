from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from data_base_connect import ForumPostDatabase, NotificationDatabase

class SingletonForumPost:
    __instance = None

    def __new__(cls, root, enrollment_id):
        if cls.__instance is None:
            cls.__instance = super(SingletonForumPost, cls).__new__(cls)
            cls.__instance.create_widget(root, enrollment_id)
            
        return cls.__instance

    def create_widget(self, root, enrollment_id):
        self.enrollment_id = enrollment_id
        self.forum_window = Toplevel(root)
        self.forum_window.title("Forum Post")
        self.forum_window.geometry("800x600")
        self.forum_window.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('DEVELOPMENT/studentify.jpg'))
        self.bgimage_label = Label(self.forum_window, image=self.bgimage)
        self.bgimage_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # New Post Section
        self.new_post_label = Label(self.forum_window, text="Create a New Post", font=("times new roman", 18), bg="white")
        self.new_post_label.place(x=50, y=10)
        
        self.post_title_label = Label(self.forum_window, text="Title", font=("times new roman", 15), bg="white")
        self.post_title_label.place(x=50, y=50)
        self.post_title_entry = Entry(self.forum_window, font=("times new roman", 15))
        self.post_title_entry.place(x=150, y=50, width=300)
        
        self.post_content_label = Label(self.forum_window, text="Content", font=("times new roman", 15), bg="white")
        self.post_content_label.place(x=50, y=100)
        self.post_content_entry = Text(self.forum_window, font=("times new roman", 15), height=5)
        self.post_content_entry.place(x=150, y=100, width=300)
        
        self.submit_post_btn = Button(self.forum_window, text="Submit Post", font=("times new roman", 15), bg="lightblue", command=lambda: self.submit_post())
        self.submit_post_btn.place(x=500, y=200)
        
        # Posts Section with Scrollbar
        self.posts_frame = Frame(self.forum_window)
        self.posts_frame.place(x=50, y=250, width=700, height=300)

        self.canvas = Canvas(self.posts_frame, bg="white")
        self.scrollbar = Scrollbar(self.posts_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.current_page = 0
        self.posts_per_page = 10
        
        self.update_posts()
        
        # Handle window close to reset instance
        self.forum_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def submit_post(self):
        title = self.post_title_entry.get()
        content = self.post_content_entry.get("1.0", END).strip()
        
        if not title or not content:
            messagebox.showerror("Error", "Title and content cannot be empty.")
        else:
            ForumPostDatabase.add_post(title, content, self.enrollment_id)
            self.clear_new_post()
            self.update_posts()

    def clear_new_post(self):
        self.post_title_entry.delete(0, END)
        self.post_content_entry.delete("1.0", END)

    def pass_name(self, user_name):
        self.user_name = user_name
    
    def update_posts(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        posts = ForumPostDatabase.get_posts(self.current_page, self.posts_per_page)
        
        for post in posts:
            post_title_label = Label(self.scrollable_frame, text=post['title'], font=("times new roman", 15, "bold"), bg="white")
            post_title_label.pack(anchor="w", pady=5)
            
            post_content_label = Label(self.scrollable_frame, text=post['content'], font=("times new roman", 15), bg="white", wraplength=650, justify=LEFT)
            post_content_label.pack(anchor="w", pady=5)
            
            comment_btn = Button(self.scrollable_frame, text="Comment", font=("times new roman", 12), bg="lightblue", command=lambda post_id=post['id']: self.add_comment(post_id, post['enrollment_id']))
            comment_btn.pack(anchor="w", pady=5)
            
            for comment in post['comments']:
                comment_label = Label(self.scrollable_frame, text=f"{comment['username']}: {comment['content']}", font=("times new roman", 12), bg="white", wraplength=650, justify=LEFT)
                comment_label.pack(anchor="w", pady=5)

        load_more_btn = Button(self.scrollable_frame, text="Load More", font=("times new roman", 15), bg="lightblue", command=self.load_more_posts)
        load_more_btn.pack(pady=10)

    def load_more_posts(self):
        self.current_page += 1
        self.update_posts()

    def add_comment(self, post_id, enrollment_id):
        name = self.user_name
        if not name:
            messagebox.showerror("Error", "Unable to fetch name.")
            return

        comment = simpledialog.askstring("Add Comment", "Enter your comment:")
        if comment:
            ForumPostDatabase.add_comment(post_id, name, comment)
            NotificationDatabase.add_notification(enrollment_id, f"Forum Post: The student {name} commented: {comment}")
            self.update_posts()

    def on_close(self):
        """Reset instance and close the window"""
        SingletonForumPost.__instance = None
        self.forum_window.destroy()

if __name__ == "__main__":
    root = Tk()
    # Simulate a user login with their enrollment ID
    # user_enrollment_id = "as"  # Replace with the actual user's enrollment ID after login
    # app = SingletonForumPost(root, user_enrollment_id)
    root.mainloop()
