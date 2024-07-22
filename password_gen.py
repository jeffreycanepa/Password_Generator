# This is a password generator.  When asked enter a number for the desired
# length of password.  The generated password will then be output to the command line.

import random

import string

# Define the character set

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):

    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():

    length = int(input("Enter the desired length for your password: "))

    password = generate_password(length)

    print(f"Generated Password: {password}")

if __name__ == "__main__":

    main()

def generate_password(length):

    if length < 4:

        raise ValueError("Password length must be at least 4")

    password = [

    random.choice(string.ascii_lowercase),

    random.choice(string.ascii_uppercase),

    random.choice(string.digits),

    random.choice(string.punctuation)

    ]

    password += random.choices(characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

