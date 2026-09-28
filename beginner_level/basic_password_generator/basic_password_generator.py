### python by moshiurr007 --> beginner_level ###

# basic password generator #

import random

def generate_password():

    alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabets_upper = alphabets_lower.upper()
    numbers = "0123456789"
    special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"

    all_characters = alphabets_lower + alphabets_upper + special_chars + numbers

    length = int(input("Enter password length: "))

    if length < 8 or length > 30:
        raise ValueError("Password length should be between 8 and 30 characters.")
    
    password = ""
    
    for _ in range(length):
        password += random.choice(all_characters)

    return password

print(generate_password())