import tkinter as tk


class CreditCardValidatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Credit Card Validator")
        root.geometry("400x200")
        self.label = tk.Label(master, text="Enter a credit card number:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Validate", command=self.validate)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def validate(self):
        card_number = self.entry.get()
        if not card_number.isdigit():
            self.result_label.config(text="Please enter a valid credit card number")
        else:
            card_type = getType(int(card_number))
            if card_type == "INVALID":
                self.result_label.config(text="INVALID", fg="red")
            else:
                if isValid(int(card_number), card_type):
                    self.result_label.config(text=card_type, fg="green")
                else:
                    self.result_label.config(text="INVALID", fg="red")


def isValid(n, type):
    """Check the validity"""
    if type == "VISA" and (len(str(n)) == 13 or len(str(n)) == 16):
        return True
    elif type == "AMEX" and len(str(n)) == 15:
        return True
    elif type == "MASTERCARD" and len(str(n)) == 16:
        return True
    else:
        return False


def getType(n):
    """Get what type of card"""
    # visa
    if int(str(n)[0]) == 4 and checksum(n):
        return "VISA"
    # amex
    elif (int(str(n)[:2]) == 34 or int(str(n)[:2]) == 37) and checksum(n):
        return "AMEX"
    # mastercard
    elif (int(str(n)[:2]) >= 51 and int(str(n)[:2]) <= 55) and checksum(n):
        return "MASTERCARD"
    else:
        return "INVALID"


def checksum(n):
    """Luhn's algorithm"""
    # multiply every other digit by 2, starting with the number’s second-to-last digit,
    # and then add those products’ digits together.
    sum = 0
    for i in range(len(str(n)) - 2, -1, -2):
        sum += int(str(n)[i]) * 2
        if int(str(n)[i]) * 2 > 9:
            sum += 1
    # add the sum to the sum of the digits that weren’t multiplied by 2.
    for i in range(len(str(n)) - 1, -1, -2):
        sum += int(str(n)[i])
    # if the total’s last digit is 0(or, put more formally, if the total modulo 10 is congruent to 0),
    # the number is valid!
    if sum % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = CreditCardValidatorGUI(root)
    root.mainloop()
