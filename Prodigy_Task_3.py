import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate strength
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Determine password strength
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = {
        "length": length_criteria,
        "uppercase": uppercase_criteria,
        "lowercase": lowercase_criteria,
        "number": number_criteria,
        "special_char": special_char_criteria
    }

    return strength, feedback

def print_feedback(password):
    strength, feedback = assess_password_strength(password)
    
    print(f"Password: {password}")
    print(f"Strength: {strength}")
    print("\nCriteria Check:")
    print(f"Length (≥ 8): {'✔️' if feedback['length'] else '❌'}")
    print(f"Uppercase Letters: {'✔️' if feedback['uppercase'] else '❌'}")
    print(f"Lowercase Letters: {'✔️' if feedback['lowercase'] else '❌'}")
    print(f"Numbers: {'✔️' if feedback['number'] else '❌'}")
    print(f"Special Characters: {'✔️' if feedback['special_char'] else '❌'}")

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to assess: ")
    print_feedback(user_password)
