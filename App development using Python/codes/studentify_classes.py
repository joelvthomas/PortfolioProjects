from datetime import datetime

class User:
    def __init__(self, first_name, last_name, matriculation_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.matriculation_id = matriculation_id
        self.password = password
        self.profile_visibility = "private"  # default visibility setting

    def login(self, matriculation_id, password):
        # Method to verify login credentials
        return self.matriculation_id == matriculation_id and self.password == password

    def reset_password(self):
        # Method to reset password
        pass

    def set_profile_visibility(self, visibility):
        # Method to set profile visibility (public, private, custom)
        self.profile_visibility = visibility

    def report_user(self, user_id):
        # Method to report another user for improper behavior
        pass

    def add_event(self, event):
        # Method to add an event
        pass

    def rsvp_event(self, event_id):
        # Method to RSVP for an event
        pass


class Event:
    def __init__(self, event_name, location, date, details, contact_details,rsvp_desdline):
        self.event_name = event_name
        self.location = location
        self.date = date
        self.details = details
        self.contact_details = contact_details
        self.participants = []
        self.rsvp_deadline = rsvp_desdline

    def add_participant(self, user):
        # Method to add a participant to the event
        self.participants.append(user)

    def notify_participants(self):
        # Method to notify participants about the event
        pass

    def set_rsvp_deadline(self, deadline):
        # Method to set RSVP deadline
        self.rsvp_deadline = deadline


class ForumPost:
    def __init__(self, user, course, post_content):
        self.user = user  # User instance
        self.course = course
        self.post_content = post_content
        self.comments = []

    def add_comment(self, comment):
        # Method to add a comment to the post
        self.comments.append(comment)

    def moderate_comments(self):
        # Method to moderate comments for inappropriate content
        pass


class Inquiry:
    def __init__(self, category, content):
        self.category = category
        self.content = content
        self.resolved = False
        self.feedback = None

    def resolve(self):
        # Method to mark inquiry as resolved
        self.resolved = True

    def provide_feedback(self, feedback):
        # Method to provide feedback on the resolution process
        self.feedback = feedback


class Notification:
    def __init__(self, message, recipient, timestamp):
        self.message = message
        self.recipient = recipient
        self.timestamp = timestamp

    def send_notification(self):
        # Method to send notification to the recipient
        pass


class Studentify:
    def __init__(self):
        self.users = []
        self.events = []
        self.forum_posts = []
        self.inquiries = []
        self.notifications = []

    def create_user_account(self, first_name, last_name, matriculation_id, password):
        # Method to create a new user account
        user = User(first_name, last_name, matriculation_id, password)
        self.users.append(user)

    def add_event(self, event_name, location, date, details, contact_details):
        # Method to add a new event
        event = Event(event_name, location, date, details, contact_details)
        self.events.append(event)

    def post_forum_question(self, user, course, post_content):
        # Method to post a question on the forum
        forum_post = ForumPost(user, course, post_content)
        self.forum_posts.append(forum_post)

    def submit_inquiry(self, category, content):
        # Method to submit an inquiry
        inquiry = Inquiry(category, content)
        self.inquiries.append(inquiry)

    def categorize_inquiry(self, inquiry):
        # Method to categorize inquiries
        pass

    def notify_users(self, message, recipient):
        # Method to send notifications to users
        notification = Notification(message, recipient, timestamp=datetime.now())
        self.notifications.append(notification)
        notification.send_notification()

    def set_event_reminder(self, event, reminder_time):
        # Method to set event reminders for users
        pass

    def set_rsvp_deadline(self, event, deadline):
        # Method to set RSVP deadline for an event
        event.set_rsvp_deadline(deadline)
