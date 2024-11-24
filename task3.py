import re

def assess_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        strength += 2
        feedback.append("Password length is strong (12+ characters).")
    elif len(password) >= 8:
        strength += 1
        feedback.append("Password length is moderate (8-11 characters).")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
        feedback.append("Includes uppercase letters.")
    else:
        feedback.append("Add uppercase letters for better strength.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
        feedback.append("Includes lowercase letters.")
    else:
        feedback.append("Add lowercase letters for better strength.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
        feedback.append("Includes numbers.")
    else:
        feedback.append("Add numbers for better strength.")

    # Check for symbols
    if any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/~`" for char in password):
        strength += 1
        feedback.append("Includes symbols.")
    else:
        feedback.append("Add symbols for better strength.")

    # Strength feedback
    if strength >= 6:
        feedback.append("Password is very strong!")
    elif 4 <= strength < 6:
        feedback.append("Password is strong, but can be improved.")
    elif 2 <= strength < 4:
        feedback.append("Password is weak. Add more complexity.")
    else:
        feedback.append("Password is very weak. Make significant improvements.")

    return "\n".join(feedback)


# Example usage
password = input("Enter a password to assess: ")
print(assess_password_strength(password))