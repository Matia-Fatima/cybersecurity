# Password Strength Checker
# Save this file as passStrengthChecker.py

import math
import string

# List of common weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "111111", "12345678",
    "abc123", "password1", "iloveyou", "123123", "admin", "letmein"
]

def analyze_password(password):
    """Check what types of characters are used in the password"""
    return {
        "length": len(password),
        "has_lower": any(c.islower() for c in password),
        "has_upper": any(c.isupper() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_symbol": any(not c.isalnum() for c in password),
        "is_common": password.lower() in COMMON_PASSWORDS
    }

def estimate_entropy(password):
    """Estimate how strong the password is mathematically (entropy)"""
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0
    entropy = len(password) * math.log2(pool)
    return entropy

def score_password(analysis, entropy):
    """Give score and strength category"""
    score = 0

    # Length points
    if analysis["length"] >= 12:
        score += 3
    elif analysis["length"] >= 8:
        score += 2
    elif analysis["length"] >= 6:
        score += 1

    # Character variety points
    score += (
        analysis["has_lower"]
        + analysis["has_upper"]
        + analysis["has_digit"]
        + analysis["has_symbol"]
    )

    # Deduct points if common
    if analysis["is_common"]:
        score -= 3

    # Entropy bonus
    if entropy >= 60:
        score += 2
    elif entropy >= 40:
        score += 1

    # Final strength category
    if score <= 1:
        strength = "Very Weak"
    elif score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Fair"
    elif score <= 7:
        strength = "Good"
    else:
        strength = "Strong"

    return score, strength

def get_suggestions(analysis):
    """Suggest how to improve the password"""
    suggestions = []
    if analysis["is_common"]:
        suggestions.append("Avoid using common passwords.")
    if analysis["length"] < 12:
        suggestions.append("Use a longer password (12+ characters).")
    if not analysis["has_upper"]:
        suggestions.append("Add uppercase letters (A-Z).")
    if not analysis["has_lower"]:
        suggestions.append("Add lowercase letters (a-z).")
    if not analysis["has_digit"]:
        suggestions.append("Include numbers (0-9).")
    if not analysis["has_symbol"]:
        suggestions.append("Include special characters (!, @, #, $, etc.)")
    if not suggestions:
        suggestions.append("Your password looks strong!")
    return suggestions

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")

    if not password:
        print("No password entered. Please try again.")
        return

    analysis = analyze_password(password)
    entropy = estimate_entropy(password)
    score, strength = score_password(analysis, entropy)
    suggestions = get_suggestions(analysis)

    print("\n--- Password Analysis ---")
    print(f"Length: {analysis['length']}")
    print(f"Has Lowercase: {analysis['has_lower']}")
    print(f"Has Uppercase: {analysis['has_upper']}")
    print(f"Has Digits: {analysis['has_digit']}")
    print(f"Has Symbols: {analysis['has_symbol']}")
    print(f"Common Password: {analysis['is_common']}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Score: {score}")
    print(f"Strength: {strength}")

    print("\n--- Suggestions ---")
    for s in suggestions:
        print(f"- {s}")

    print("\n Check complete! Stay safe online.")

if __name__ == "__main__":
    main()
