import sqlite3
import tensorflow as tf
import numpy as np

from user import User
from user import NewUser
 

class LoginDatabase:

    @staticmethod
    def _get_connection():
        connection = sqlite3.connect("DEVELOPMENT/database/login_database.db")
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user(name VARCHAR, enrollment_id VARCHAR PRIMARY KEY, account_type VARCHAR, email VARCHAR, password VARCHAR);")
        return connection, cursor 
     
    
        

    @staticmethod
    def is_existing_user(current_user:User):
        
        enrollment_id = current_user.get_enrollment_id()
        user_passw = current_user.get_userpassw()
         
        conn, cursor = LoginDatabase._get_connection()
        cursor.execute("SELECT * FROM user WHERE enrollment_id=? AND password=?",(enrollment_id,user_passw))
        row = cursor.fetchone()
        conn.close()
        return row
    
    @staticmethod
    def get_user_details(enrollment_id):
        conn, cursor = LoginDatabase._get_connection()
        cursor.execute("SELECT enrollment_id, name, email FROM user WHERE enrollment_id = ?", (enrollment_id,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return {"enrollment_id": user[0], "name": user[1], "email": user[2]}
        return None
    
       
    @staticmethod
    def upload_data(new_user:NewUser):
        dict=new_user.get_user_data()
        conn, cursor = LoginDatabase._get_connection()
        cursor.execute("INSERT INTO user (name,enrollment_id, account_type, email, password)VALUES (?,?,?,?,?)",
                                     (dict["enrollment_id"], dict["name"], dict["account_type"], dict["email"], dict["password"]))

        conn.commit()
        conn.close()


class EventDatabase:

    @staticmethod
    def _get_connection():
        connection = sqlite3.connect("DEVELOPMENT/database/event_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS event(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location VARCHAR,
                event_name VARCHAR,
                date VARCHAR,
                time VARCHAR,
                about TEXT,
                host VARCHAR,
                host_id VARCHAR
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rsvp(
                event_id INTEGER,
                username VARCHAR,
                rsvp_event VARCHAR,
                FOREIGN KEY(event_id) REFERENCES event(id)
            );
        """)  
        return connection, cursor

    @staticmethod
    def add_event(location, event_name, date, time, about, host,host_id):
        conn, cursor = EventDatabase._get_connection()
        cursor.execute("INSERT INTO event (location, event_name, date, time, about, host, host_id) VALUES (?, ?, ?, ?, ?, ?,?)",
                       (location, event_name, date, time, about, host, host_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_events():
        conn, cursor = EventDatabase._get_connection()
        cursor.execute("SELECT * FROM event")
        events = cursor.fetchall()
        conn.close()
        return events

    @staticmethod
    def add_rsvp(event_id, username,rsvp_event):
        conn, cursor = EventDatabase._get_connection()
        cursor.execute("INSERT INTO rsvp (event_id, username, rsvp_event) VALUES (?, ?, ?)", (event_id, username,rsvp_event))
        conn.commit()
        conn.close()

    @staticmethod
    def get_event_rsvps(event_id):
        conn, cursor = EventDatabase._get_connection()
        cursor.execute("SELECT username,rsvp_event FROM rsvp WHERE event_id=?", (event_id,))
        rsvps = cursor.fetchall()
        conn.close()
        return [rsvp for rsvp in rsvps]
    
    @staticmethod
    def get_event_host(event_id):
        conn, cursor = EventDatabase._get_connection()
        cursor.execute("SELECT host_id FROM event WHERE id=?", (event_id,))
        host = cursor.fetchone()
        conn.close()
        return host[0] if host else None


class InquiryDatabase:

    @staticmethod
    def _get_connection():
        connection = sqlite3.connect("DEVELOPMENT/database/inquiry_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inquiry(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                enrollment_id VARCHAR,
                email VARCHAR,
                department VARCHAR,
                inquiry_type VARCHAR,
                subject VARCHAR,
                details TEXT,
                status VARCHAR DEFAULT 'Open'
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reply(
                inquiry_id INTEGER,
                replier_id VARCHAR,
                reply TEXT,
                FOREIGN KEY(inquiry_id) REFERENCES inquiry(id)
            );
        """)
        return connection, cursor

    @staticmethod
    def add_inquiry(name, enrollment_id, email, department, inquiry_type, subject, details):
        conn, cursor = InquiryDatabase._get_connection()
        cursor.execute("INSERT INTO inquiry (name, enrollment_id, email, department, inquiry_type, subject, details) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, enrollment_id, email, department, inquiry_type, subject, details))
        conn.commit()
        conn.close()

    @staticmethod
    def get_inquiries():
        conn, cursor = InquiryDatabase._get_connection()
        cursor.execute("SELECT * FROM inquiry WHERE status = 'Open'")
        inquiries = cursor.fetchall()
        conn.close()
        return inquiries

    @staticmethod
    def add_reply(inquiry_id, replier_id, reply):
        conn, cursor = InquiryDatabase._get_connection()
        cursor.execute("INSERT INTO reply (inquiry_id, replier_id, reply) VALUES (?, ?, ?)", (inquiry_id, replier_id, reply))
        cursor.execute("UPDATE inquiry SET status = 'Closed' WHERE id = ?", (inquiry_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_replies(inquiry_id):
        conn, cursor = InquiryDatabase._get_connection()
        cursor.execute("SELECT reply FROM reply WHERE inquiry_id=?", (inquiry_id,))
        replies = cursor.fetchall()
        conn.close()
        return [reply[0] for reply in replies]

class ForumPostDatabase:

    @staticmethod
    def _get_connection():
        connection = sqlite3.connect("DEVELOPMENT/database/forum_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR,
                content TEXT,
                enrollment_id VARCHAR
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER,
                username VARCHAR,
                content TEXT,
                FOREIGN KEY(post_id) REFERENCES posts(id)
            );
        """)
        return connection, cursor

    @staticmethod
    def add_post(title, content,enrollment_id):
        conn, cursor = ForumPostDatabase._get_connection()
        cursor.execute("INSERT INTO posts (title, content, enrollment_id) VALUES (?, ?, ?)", (title, content,enrollment_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_posts(page=0, per_page=10):
        conn, cursor = ForumPostDatabase._get_connection()
        offset = page * per_page
        cursor.execute("SELECT id, title, content, enrollment_id FROM posts ORDER BY id DESC LIMIT ? OFFSET ?", (per_page, offset))
        posts = cursor.fetchall()
        result = []
        for post in posts:
            post_id, title, content,enrollment_id = post
            cursor.execute("SELECT username, content FROM comments WHERE post_id = ?", (post_id,))
            comments = cursor.fetchall()
            result.append({
                'id': post_id,
                'title': title,
                'content': content,
                'enrollment_id' : enrollment_id,
                'comments': [{'username': comment[0], 'content': comment[1]} for comment in comments]
            })
        conn.close()
        return result

    @staticmethod
    def add_comment(post_id, username, content):
        conn, cursor = ForumPostDatabase._get_connection()
        cursor.execute("INSERT INTO comments (post_id, username, content) VALUES (?, ?, ?)", (post_id, username, content))
        conn.commit()
        conn.close()


class NotificationDatabase:
    @staticmethod
    def _get_connection():
        connection = sqlite3.connect("DEVELOPMENT/database/notification_database.db")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR,
                content TEXT,
                status VARCHAR DEFAULT 'Unread'
            );
        """)
        return connection, cursor

    @staticmethod
    def add_notification(user_id, content):
        conn, cursor = NotificationDatabase._get_connection()
        cursor.execute("INSERT INTO notifications (user_id, content) VALUES (?, ?)", (user_id, content))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user_notifications(user_id):
        conn, cursor = NotificationDatabase._get_connection()
        cursor.execute("SELECT content FROM notifications WHERE user_id=? AND status='Unread'", (user_id,))
        notifications = cursor.fetchall()
        conn.close()
        return [notif[0] for notif in notifications]

    @staticmethod
    def mark_as_read(user_id):
        conn, cursor = NotificationDatabase._get_connection()
        cursor.execute("UPDATE notifications SET status='Read' WHERE user_id=?", (user_id,))
        conn.commit()
        conn.close()