import re
import random
from getpass import getpass

print("Test how strong your password is. This program looks for weaknesses in passwords like length, number and symbol usage.")


def create_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    password = "".join(random.choice(chars) for _ in range(12))
    print("Your password is too weak. Here is a randomly generated password:", password)


# Define a list of commonly used words and phrases to check against
common_passwords = [
    "password",
    "PASSWORD",
    "Password",
    "p@ssword",
    "P@ssword",
    "Pa$$word",
    "pa$$word",
    "passw0rd",
    "Passw0rd",
    "p@ssw0rd",
    "P@ssw0rd",
    "Pa$$w0rd",
    "pa$$w0rd",
    "p@55word",
    "P@55word",
    "Pa$$w0rd!",
    "password123",
    "qwerty123",
    "welcome123",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "letmein",
    "monkey",
    "sunshine",
    "iloveyou",
    "admin",
    "welcome",
    "football",
    "login",
    "admin123",
    "qwerty123",
    "welcome123",
]

# Define the minimum length for the password
min_length = 8

# Get the password from the user
password = getpass("Enter your password: ")

# Check if the password is a commonly used password
if password in common_passwords:
    print("You are using a common password. Please change it to a stronger password.")

# Check the password against requirements
elif len(password) < min_length:
    print("Password is too short. Please choose a password that is at least", min_length, "characters long.")

else:
    # Define a list of password requirements to check against
    requirements = [
        {"name": "Uppercase letters", "regex": r"[A-Z]", "score": 1},
        {"name": "Lowercase letters", "regex": r"[a-z]", "score": 1},
        {"name": "Numbers", "regex": r"\d", "score": 1},
        {"name": "Symbols", "regex": r"[^\w\s]", "score": 1},
        {"name": "Consecutive letters", "regex": r"[a-zA-Z]{2}", "score": -1},
        {"name": "Consecutive numbers", "regex": r"\d{2,}", "score": -1},
        {"name": "Repeating characters", "regex": r"(.)\1{2,}", "score": -1},
        {"name": "Keyboard patterns", "regex": r"qwert[yuiop]|asdf[ghjkl]|zxcvb[nm]", "score": -1},
    ]

    # Check the password against each requirement and calculate a score
    score = 0
    for req in requirements:
        matches = re.findall(req["regex"], password)
        if len(matches) > 0:
            score += req["score"]

    # Generate a random password if the score is negative
    if score < 0:
        create_password()

    # Provide feedback to the user based on their password score
    else:
        if score <= 2:
            create_password()
        elif score <= 4:
            print("Your password is moderate.")
        else:
            print("Your password is strong.")
