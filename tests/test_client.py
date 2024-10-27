import unittest
from src.client import create_user

class TestUserFunctions(unittest.TestCase):
    
    def test_create_user_valid(self):
        result = create_user("john_doe", "john@example.com")
        self.assertEqual(result, "User created: john_doe")
    
    def test_create_user_invalid_username(self):
        result = create_user(123, "john@example.com")
        self.assertEqual(result, "Username must be a string")
    
    def test_create_user_invalid_email(self):
        result = create_user("john_doe", 123)
        self.assertEqual(result, "Email must be a string")
    
    def test_create_user_invalid_email_format(self):
        result = create_user("john_doe", "invalid_email")
        self.assertEqual(result, "Email is invalid")
    
    def test_create_user_another_valid(self):
        result = create_user("jane_doe", "jane@example.com")
        self.assertEqual(result, "User created: jane_doe")
    


if __name__ == '__main__':
    unittest.main()
