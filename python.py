# Python source code

def main():
    """Ask for the number."""
    n = int(input("Number: "))

    type = getType(n)
    if (type == "INVALID"):
        print("INVALID")
    else:
        if (isValid(n, type)):
            print(type)
        else:
            print("INVALID")


def isValid(n, type):
    """Check the validity"""
    if (type == "VISA" and (len(str(n)) == 13 or len(str(n)) == 16)):
        return True
    elif (type == "AMEX" and len(str(n)) == 15):
        return True
    elif (type == "MASTERCARD" and len(str(n)) == 16):
        return True
    else:
        return False


def getType(n):
    """Get what type of card"""
    # visa
    if (int(str(n)[0]) == 4 and checksum(n)):
        return "VISA"
    # amex
    elif ((int(str(n)[:2]) == 34 or int(str(n)[:2]) == 37) and checksum(n)):
        return "AMEX"
    # mastercard
    elif ((int(str(n)[:2]) >= 51 and int(str(n)[:2]) <= 55) and checksum(n)):
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
        if (int(str(n)[i]) * 2 > 9):
            sum += 1
    # add the sum to the sum of the digits that weren’t multiplied by 2.
    for i in range(len(str(n)) - 1, -1, -2):
        sum += int(str(n)[i])
    # if the total’s last digit is 0(or, put more formally, if the total modulo 10 is congruent to 0),
    # the number is valid!
    if (sum % 10 == 0):
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    main()
