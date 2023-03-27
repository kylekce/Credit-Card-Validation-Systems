# Credit Card Validator GUI 
# Test for Mac

# tkinter is a Python library for creating GUIs
# ToolKit Interface
import tkinter as tk
import re


class CreditCardValidatorGUI:
    """Class blueprint for the Credit Card Validator GUI."""
    def __init__(self, master):
        # Initialize the master window with a title and size
        self.master = master
        master.title("Credit Card Validator")
        master.geometry("400x200")
        
        # Add a label for the user to enter a credit card number
        self.label = tk.Label(master, text="Enter a credit card number:")
        self.label.pack()

        # Add an entry widget for the user to input the credit card number
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Add a frame to hold the Validate and Reset buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        # Add a button that triggers the validation process
        self.validate_button = tk.Button(self.button_frame, text="Validate", command=self.validate)
        self.validate_button.pack(side=tk.LEFT, padx=(0, 10))

        # Add a button to reset the input field
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        # Add a label to display the result of the validation
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
        # Periodically update the GUI to reduce flickering
        self.update()


    def update(self):
        """Method to periodically update the GUI."""
        self.master.after(10, self.update)
     
        
    def validate(self):
        """Method to validate the credit card number."""
        # Get the credit card number from the entry widget and remove any trailing spaces
        card_number = self.entry.get().rstrip()
        
        # Check if the input is a valid credit card number (contains only digits and optional spaces)
        if not re.match("^[0-9]+(\s*[0-9]+)*$", card_number):
            self.result_label.config(text="Please enter a valid credit card number")
        else:
            # Remove any spaces from the credit card number
            card_number = card_number.replace(" ", "")
            
            # Determine the type of credit card
            card_type = get_type(int(card_number))
            
            # If the card is invalid, display "INVALID" in red text
            if card_type == "INVALID":
                self.result_label.config(text="INVALID", fg="red")
            else:
                # If the card is valid, display its type in green text
                if is_valid(int(card_number), card_type):
                    self.result_label.config(text=card_type, fg="green")
                # If the card is not valid, display "INVALID" in red text
                else:
                    self.result_label.config(text="INVALID", fg="red")

                    
    def reset(self):
        """Method to reset the input field and result label."""
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")


def is_valid(n, type):
    """Function to check if a credit card number is valid for a given type."""
    # Check the length and starting digits of the credit card number for the given type
    if type == "VISA" and (len(str(n)) == 13 or len(str(n)) == 16):
        return True
    elif type == "AMEX" and len(str(n)) == 15:
        return True
    elif type == "MASTERCARD" and len(str(n)) == 16:
        return True
    else:
        return False


def get_type(n):
    """Function to determine the type of a credit card number."""
    # Check the starting digits of the credit card number to determine its type
    # and call the check_sum function to validate the number
    if int(str(n)[0]) == 4 and check_sum(n):
        return "VISA"
    elif (int(str(n)[:2]) == 34 or int(str(n)[:2]) == 37) and check_sum(n):
        return "AMEX"
    elif (int(str(n)[:2]) >= 51 and int(str(n)[:2]) <= 55) and check_sum(n):
        return "MASTERCARD"
    else:
        return "INVALID"


def check_sum(n):
    """Function to validate a credit card number using Luhn's algorithm."""
    # Initialize a sum variable and loop through the digits of the credit card number
    sum = 0
    for i in range(len(str(n)) - 2, -1, -2):
        # Multiply every other digit by 2, starting 
        # with the second-to-last digit, and add the digits of the products together
        sum += int(str(n)[i]) * 2
        if int(str(n)[i]) * 2 > 9:
            sum += 1
        
    # Add the sum to the sum of the digits that weren't multiplied by 2
    for i in range(len(str(n)) - 1, -1, -2):
        sum += int(str(n)[i])
        
    # If the last digit of the sum is 0, the credit card number is valid
    if sum % 10 == 0:
        return True
    else:
        return False

        
if __name__ == "__main__":
    root = tk.Tk()
    my_gui = CreditCardValidatorGUI(root)
    root.mainloop()