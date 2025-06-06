import random
import string
import secrets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

def check_password_strength(password):
    """Check password strength based on length and character diversity."""
    strength = "Weak"
    if len(password) >= 12:
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    return strength

def generate_password(length, include_uppercase, include_digits, include_special):
    character_pool = lowercase
    if include_uppercase:
        character_pool += uppercase
    if include_digits:
        character_pool += digits
    if include_special:
        character_pool += special_characters

    password_chars = []
    if include_uppercase:
        password_chars.append(secrets.choice(uppercase))
    if include_digits:
        password_chars.append(secrets.choice(digits))
    if include_special:
        password_chars.append(secrets.choice(special_characters))

    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(character_pool) for _ in range(remaining_length)]
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

password_length = int(input("Enter the length of the password: "))
while password_length < 6:
    print("Password length must be at least 6 characters.")
    password_length = int(input("Enter the length of the password: "))

include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'
generated_password = generate_password(password_length, include_uppercase, include_digits, include_special)
strength = check_password_strength(generated_password)


print(f"Your generated password is: {generated_password}")
print(f"Password strength: {strength}")