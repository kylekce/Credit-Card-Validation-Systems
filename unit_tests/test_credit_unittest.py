"""
To run the tests, unittest is a built-in module in Python, so you don't need to install it.

Run the command in your terminal:
python -m unittest test_credit_unittest.py

This means that you are running the unittest module as a script, 
and passing the name of the file that contains the tests.
"""

import unittest
import tkinter as tk
from credit_gui import CreditCardValidatorGUI, is_valid, get_type, check_sum

class TestCreditCardValidator(unittest.TestCase):
    """Test the CreditCardValidatorGUI class and its methods."""
    def test_gui_creation(self):
        """Test that the GUI is created correctly."""
        root = tk.Tk()
        gui = CreditCardValidatorGUI(root)

        self.assertIsInstance(gui.master, tk.Tk)
        self.assertIsInstance(gui.label, tk.Label)
        self.assertIsInstance(gui.entry, tk.Entry)
        self.assertIsInstance(gui.button_frame, tk.Frame)
        self.assertIsInstance(gui.validate_button, tk.Button)
        self.assertIsInstance(gui.reset_button, tk.Button)
        self.assertIsInstance(gui.result_label, tk.Label)
    
    def test_is_valid(self):
        """Test that the is_valid function works correctly."""
        self.assertTrue(is_valid(378282246310005, "AMEX"))
        self.assertTrue(is_valid(371449635398431, "AMEX"))
        self.assertTrue(is_valid(5555555555554444, "MASTERCARD"))
        self.assertTrue(is_valid(5105105105105100, "MASTERCARD"))
        self.assertTrue(is_valid(4111111111111111, "VISA"))
        self.assertTrue(is_valid(4012888888881881, "VISA"))
        self.assertFalse(is_valid(37828224631000, "AMEX"))
        self.assertFalse(is_valid(37144963539843, "AMEX"))
        self.assertFalse(is_valid(555555555555444, "MASTERCARD"))
        self.assertFalse(is_valid(510510510510510, "MASTERCARD"))
        self.assertFalse(is_valid(411111111111111, "VISA"))
        self.assertFalse(is_valid(401288888888188, "VISA"))
        
    def test_get_type(self):
        """Test that the get_type function works correctly."""
        self.assertEqual(get_type(378282246310005), "AMEX")
        self.assertEqual(get_type(371449635398431), "AMEX")
        self.assertEqual(get_type(5555555555554444), "MASTERCARD")
        self.assertEqual(get_type(5105105105105100), "MASTERCARD")
        self.assertEqual(get_type(4111111111111111), "VISA")
        self.assertEqual(get_type(4012888888881881), "VISA")
        self.assertEqual(get_type(37828224631000), "INVALID")
        self.assertEqual(get_type(37144963539843), "INVALID")
        self.assertEqual(get_type(555555555555444), "INVALID")
        self.assertEqual(get_type(510510510510510), "INVALID")
        self.assertEqual(get_type(411111111111111), "INVALID")
        self.assertEqual(get_type(401288888888188), "INVALID")
        
    def test_check_sum(self):
        """Test that the check_sum function works correctly."""
        self.assertTrue(check_sum(378282246310005))
        self.assertTrue(check_sum(371449635398431))
        self.assertTrue(check_sum(5555555555554444))
        self.assertTrue(check_sum(5105105105105100))
        self.assertTrue(check_sum(4111111111111111))
        self.assertTrue(check_sum(4012888888881881))
        self.assertFalse(check_sum(37828224631000))
        self.assertFalse(check_sum(37144963539843))
        self.assertFalse(check_sum(555555555555444))
        self.assertFalse(check_sum(510510510510510))
        self.assertFalse(check_sum(411111111111111))
        self.assertFalse(check_sum(401288888888188))
        
        
if __name__ == '__main__':
    unittest.main()
