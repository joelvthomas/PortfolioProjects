# Define the class
from studentify_classes import User
from studentify_classes import Event

# Define the unittest class
import unittest

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Event("Party", "Club", "2024-12-31", "New Year Party", "contact@hsrw.org")

    def test_initialization(self):
        self.assertEqual(self.event.event_name, "Party")
        self.assertEqual(self.event.location, "Club")
        self.assertEqual(self.event.date, "2024-12-31")
        self.assertEqual(self.event.details, "New Year Party")
        self.assertEqual(self.event.contact_details, "contact@hsrw.org")
        self.assertEqual(self.event.participants, [])
        self.assertIsNone(self.event.rsvp_deadline)

    def test_add_participant(self):
        user = User("John", "sea", "12345", "password123")
        self.event.add_participant(user)
        self.assertIn(user, self.event.participants)

  
unittest.main()




