import random
import string

def generate_password(length=12):
    """Generate a strong and secure password.

    Args:
        length (int): Length of the password (default is 12).

    Returns:
        str: A strong and secure password.
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = random.choice(uppercase_letters) + \
               random.choice(lowercase_letters) + \
               random.choice(digits) + \
               random.choice(special_characters)

    # Generate remaining characters randomly
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    print("Welcome to the Strong Password Generator!")
    print("This program will generate strong and secure passwords for you.")

    length = int(input("Enter the desired length of the password (default is 12): ") or 12)
    num_passwords = int(input("Enter the number of passwords to generate: "))

    print("\nGenerated Passwords:")
    for idx in range(num_passwords):
        password = generate_password(length)
        print(f"Password {idx + 1}: {password}")

    print("\nThank you for using the Strong Password Generator. Stay safe!")
