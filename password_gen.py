# This is a password generator. Script will ask for a password length and then return
# a randomly generated password of that length using characters from sting.ascii_letters,
# string.digits and string.punctuation.
#
# Code based on a project from Geeksided.com. 
# (https://geeksided.com/posts/step-by-step-guide-to-creating-a-python-password-generator-01j1w7jr23wr)
#

# Import necessary libs.
import random
import string

# Define the character set
characters = string.ascii_letters + string.digits + string.punctuation

# generate_password(length): 
def generate_password(length):

    if length < 4:

        raise ValueError("Password length must be at least 8 characters long.")

    password = [

        random.choice(string.ascii_lowercase),

        random.choice(string.ascii_uppercase),

        random.choice(string.digits),

        random.choice(string.punctuation)

    ]

    password += random.choices(characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

# Main(): ask user for password length, call generate_password(length), and output the result
def main():

    length = int(input("Enter the desired length for your password: "))

    password = generate_password(length)

    print(f"Generated Password: {password}")

if __name__ == "__main__":

    main()

