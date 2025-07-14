import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for desired password length
try:
    user_length = int(input("Enter the desired length of the password: "))
    if user_length < 4:
        print("Password should be at least 4 characters long for better security.")
    else:
        generated = generate_password(user_length)
        print("\nYour Generated Password is:", generated)
except ValueError:
    print("Please enter a valid number.")
