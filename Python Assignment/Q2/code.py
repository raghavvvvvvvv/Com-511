import re

def is_valid_full_name(full_name):
    # Check if the full name contains at least 2 words separated by a space
    return len(full_name.split()) >= 2

def get_full_name():
    while True:
        full_name = input("Type your full name: ")
        if is_valid_full_name(full_name):
            return full_name
        else:
            print("Please enter your full name!")

def is_valid_password(password):
    # Check if the password has at least 8 characters, 1 digit, and 1 uppercase letter
    return len(password) >= 8 and re.search(r'\d', password) and re.search(r'[A-Z]', password)

def get_password():
    while True:
        password = input("Type your password: ")
        if is_valid_password(password):
            return password
        else:
            print("Password must be of 8 or more characters in length with at least 1 digit and 1 capital letter")

def extract_first_name(full_name):
    # Split the full name and return the first word as the first name
    return full_name.split()[0]

def main():
    full_name = get_full_name()
    password = get_password()
    first_name = extract_first_name(full_name)
    print(f"Hello {first_name}")
    print("Thank you for joining us!")

if __name__ == "__main__":
    main()
