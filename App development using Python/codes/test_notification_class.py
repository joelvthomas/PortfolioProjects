from datetime import datetime
import unittest
from studentify_classes import Notification


# Define the unittest class
class TestNotification(unittest.TestCase):
    def setUp(self):
        self.notification = Notification("Event Reminder", "user123", datetime.now())

    def test_initialization(self):
        self.assertEqual(self.notification.message, "Event Reminder")
        self.assertEqual(self.notification.recipient, "user123")
        self.assertIsInstance(self.notification.timestamp, datetime)

    # Add more tests as needed for other methods when implemented



unittest.main()