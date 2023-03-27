"""
To run the tests, first install pytest if you haven't already:
pip install pytest

Then, run the pytest command in your terminal:
pytest test_credit_pytest.py
"""

import pytest
import tkinter as tk
from credit_gui import CreditCardValidatorGUI, is_valid, get_type, check_sum
    
    
def test_gui_creation():
    """Test that the GUI is created correctly."""
    root = tk.Tk()
    gui = CreditCardValidatorGUI(root)

    assert isinstance(gui.master, tk.Tk)
    assert isinstance(gui.label, tk.Label)
    assert isinstance(gui.entry, tk.Entry)
    assert isinstance(gui.button_frame, tk.Frame)
    assert isinstance(gui.validate_button, tk.Button)
    assert isinstance(gui.reset_button, tk.Button)
    assert isinstance(gui.result_label, tk.Label)
        
    
def test_is_valid():
    """Test that the is_valid function works correctly."""
    assert is_valid(378282246310005, "AMEX")
    assert is_valid(371449635398431, "AMEX")
    assert is_valid(5555555555554444, "MASTERCARD")
    assert is_valid(5105105105105100, "MASTERCARD")
    assert is_valid(4111111111111111, "VISA")
    assert is_valid(4012888888881881, "VISA")
    assert not is_valid(37828224631000, "AMEX")
    assert not is_valid(37144963539843, "AMEX")
    assert not is_valid(555555555555444, "MASTERCARD")
    assert not is_valid(510510510510510, "MASTERCARD")
    assert not is_valid(411111111111111, "VISA")
    assert not is_valid(401288888888188, "VISA")
    
    
def test_get_type():
    """Test that the get_type function works correctly."""
    assert get_type(378282246310005) == "AMEX"
    assert get_type(371449635398431) == "AMEX"
    assert get_type(5555555555554444) == "MASTERCARD"
    assert get_type(5105105105105100) == "MASTERCARD"
    assert get_type(4111111111111111) == "VISA"
    assert get_type(4012888888881881) == "VISA"
    assert get_type(37828224631000) == "INVALID"
    assert get_type(37144963539843) == "INVALID"
    assert get_type(555555555555444) == "INVALID"
    assert get_type(510510510510510) == "INVALID"
    assert get_type(411111111111111) == "INVALID"
    assert get_type(401288888888188) == "INVALID"
    

def test_check_sum():
    """Test that the check_sum function works correctly."""
    assert check_sum(378282246310005)
    assert check_sum(371449635398431)
    assert check_sum(5555555555554444)
    assert check_sum(5105105105105100)
    assert check_sum(4111111111111111)
    assert check_sum(4012888888881881)
    assert not check_sum(37828224631000)
    assert not check_sum(37144963539843)
    assert not check_sum(555555555555444)
    assert not check_sum(510510510510510)
    assert not check_sum(411111111111111)
    assert not check_sum(401288888888188)
    