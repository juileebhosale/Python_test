import unittest


def hello_world():
    """Returns a Hello World greeting."""
    return "Hello, World!"


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""

    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        self.assertIsInstance(result, str)

    def test_hello_world_content(self):
        """Test that hello_world returns the correct message."""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")

    def test_hello_world_not_empty(self):
        """Test that hello_world does not return an empty string."""
        result = hello_world()
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()
