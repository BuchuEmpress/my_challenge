# Password analyzer


# list of passwords to try from
trial_passwords  = [
    'password', '123456', '123456789', 'qwerty', 'abc123', '111111',
    '12345678', 'password1', '12345', '1234567', 'dragon', 'sunshine',
    'iloveyou', 'princess', 'admin', 'welcome', '666666', 'football',
    'password123', '123123'
]

def check_password_strength(password):
    """
    Checks whether the password contains uppercase, lowercase, digits,
    and special characters. Returns a dictionary with boolean flags.
    """
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    return {
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special
    }

def analyze_password(password):
    """
    Analyzes the password based on multiple criteria and returns the score,
    strength level, and suggestions.
    """
    score = 0
    suggestions = []

    # 1. Length check
    length_ok = len(password) >= 8
    if length_ok:
        score += 20
    else:
        suggestions.append("Increase length to at least 8 characters.")

    # 2. Character composition check using the helper function
    strength_flags = check_password_strength(password)

    if strength_flags['has_upper']:
        score += 20
    else:
        suggestions.append("Add uppercase letters.")

    if strength_flags['has_lower']:
        score += 20
    else:
        suggestions.append("Add lowercase letters.")

    if strength_flags['has_digit']:
        score += 20
    else:
        suggestions.append("Add numbers.")

    if strength_flags['has_special']:
        score += 20
    else:
        suggestions.append("Add special characters (!@#$%^&*).")

    # 3. Check against common passwords
    if password.lower() in trial_passwords:
        common_password_flag = True
    else:
        common_password_flag = False

    # Determine strength level based on total score
    if score <= 40:
        strength = "Weak"
    elif score <= 60:
        strength = "Fair"
    elif score <= 80:
        strength = "Good"
    elif score <= 100:
        strength = "Strong"
    else:
        strength = "Excellent"

    return {
        'score': score,
        'strength': strength,
        'length_ok': length_ok,
        'strength_flags': strength_flags,
        'common_password': common_password_flag,
        'suggestions': suggestions
    }

def generate_report(password):
    """
    Generates and prints the analysis report for the password.
    """
    analysis = analyze_password(password)

    print("🔒 SECURITY ANALYSIS RESULTS")
    print(f"Password: {password}")
    print(f"Score: {analysis['score']}/120 ({analysis['strength']})\n")

    # Display criteria checks with icons
    criteria_checks = [
        ("Length requirement (8+ chars)", analysis['length_ok']),
        ("Contains uppercase letters", analysis['strength_flags']['has_upper']),
        ("Contains lowercase letters", analysis['strength_flags']['has_lower']),
        ("Contains numbers", analysis['strength_flags']['has_digit']),
        ("Contains special characters", analysis['strength_flags']['has_special']),
        ("Not a common password", not analysis['common_password'])
    ]

    for description, passed in criteria_checks:
        symbol = "✅   " if passed else "❌   "
        print(f"{symbol} {description}")

    # Warning for common password
    if analysis['common_password']:
        print("\nWarning!! --> Common password detected!")

    # Suggestions
    if analysis['suggestions']:
        print("\n💡 SUGGESTIONS:")
        for suggestion in analysis['suggestions']:
            print(f"- {suggestion}")

if __name__ == "__main__":
    user_password = input("Enter password to analyze: ")
    generate_report(user_password)