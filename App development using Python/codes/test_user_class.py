import unittest
from studentify_classes import User
#from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Akhil", "Joe", "30012", "password123")

    def test_login_success(self):
        self.assertTrue(self.user.login("30012", "password123"))

    def test_login_failure(self):
        self.assertFalse(self.user.login("30012", "wrongpassword"))

    def test_login_wrong_matriculation_id(self):
        self.assertFalse(self.user.login("54321", "password123"))


    
unittest.main()
