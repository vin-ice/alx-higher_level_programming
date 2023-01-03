""""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Contains methods for testing the function,
     max_integer
    """

    def test_args_type(self):
        """Tests types accepted"""
        with self.assertRaises(TypeError):
            max_integer(11)

    def test_length(self):
        """Carries out tests on max_integer"""
        self.assertEqual(max_integer([]), None)
        
    def test_numbers(self):
        """Tests operation on number types"""
        self.assertEqual(max_integer([-12.23, -123, -0.3]), -0.3)
        self.assertEqual(max_integer(["a", "b", "r", "m"]), "r")