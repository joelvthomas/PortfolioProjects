
import unittest
from studentify_classes import User
from studentify_classes import ForumPost
from non_moderate_words import non_moderate

class TestForumPost(unittest.TestCase):
    def setUp(self):
        user = User("John", "sea", "12345", "password123")
        self.forum_post = ForumPost(user, "Mathematics", "What is calculus?")

    def test_initialization(self):
        self.assertEqual(self.forum_post.user.first_name, "John")
        self.assertEqual(self.forum_post.course, "Mathematics")
        self.assertEqual(self.forum_post.post_content, "What is calculus?")
        self.assertEqual(self.forum_post.comments, [])

    def test_add_comment(self):
        self.forum_post.add_comment("It is a branch of mathematics.")
        self.assertIn("It is a branch of mathematics.", self.forum_post.comments)  #vanilla examples

    # Add more tests as needed for other methods when implemented
    def test_moderate_comments(self):
         def test_moderate_comments(self):
            # Adding some comments
            self.forum_post.add_comment("It is a branch of mathematics.")
            self.forum_post.add_comment("You are stupid.")
            self.forum_post.add_comment("It involves limits and derivatives.")
            self.forum_post.add_comment("This is dumb.")
            
            # Apply moderation
            self.forum_post.moderate_comments()
            
            # Check if inappropriate comments are removed
            self.assertNotIn("You are stupid.", self.forum_post.comments)
            self.assertNotIn("This is dumb.", self.forum_post.comments)
            self.assertIn("It is a branch of mathematics.", self.forum_post.comments)
            self.assertIn("It involves limits and derivatives.", self.forum_post.comments)


unittest.main()
