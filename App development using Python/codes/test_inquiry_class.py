import unittest
from studentify_classes import Inquiry

class TestInquiry(unittest.TestCase):
    def setUp(self):
        self.inquiry = Inquiry("Technical", "My account is locked.")

    def test_initialization(self):
        self.assertEqual(self.inquiry.category, "Technical")
        self.assertEqual(self.inquiry.content, "My account is locked.")
        self.assertFalse(self.inquiry.resolved)
        self.assertIsNone(self.inquiry.feedback)

    def test_resolve(self):
        self.inquiry.resolve()
        self.assertTrue(self.inquiry.resolved)

    def test_provide_feedback(self):
        self.inquiry.provide_feedback("Resolved quickly")
        self.assertEqual(self.inquiry.feedback, "Resolved quickly")


    unittest.main()