### python by moshiurr007 --> intermediate_level ###

# strong password generator #

import secrets
import string

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_chars = "!@#$%^&*()=+[:;]<./,>?"
    all_characters = lowercase + uppercase + numbers + special_chars
    
    length = int(input("Enter password length: "))

    if length < 8 or length > 30:
        raise ValueError("Password length should be between 8 and 30 characters.")
    
    password = [ # ensure at least one character from each category
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(special_chars)
    ]

    for _ in range(length - 4): # fill the remained position
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password) # shuffle

    password = "".join(password)

    return password

print(generate_password())