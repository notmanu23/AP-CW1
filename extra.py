import re

# Simplified table columns for easier access
cols = {
    1: "id",
    2: "passwd",
    3: "des"
}


# Function to validate strong passwords
def validate():
    while True:
        password = input("Enter a password for the master password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Good Password!")
            return password
