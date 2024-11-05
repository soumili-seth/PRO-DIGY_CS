import re

def assess_password_strength(password):
    
    strength_assessment = {
        'length': False,
        'upper_case': False,
        'lower_case': False,
        'number': False,
        'special_char': False
    }

    # Check password length
    if len(password) >= 12:
        strength_assessment['length'] = True

    # Check for upper case letters
    if re.search(r"[A-Z]", password):
        strength_assessment['upper_case'] = True

    # Check for lower case letters
    if re.search(r"[a-z]", password):
        strength_assessment['lower_case'] = True

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength_assessment['number'] = True

    # Check for special characters
    if re.search(r"[^A-Za-z0-9]", password):
        strength_assessment['special_char'] = True

    return strength_assessment

def provide_feedback(strength_assessment):
    
    print("Password Strength Assessment:")
    print("---------------------------")

    if strength_assessment['length']:
        print("Length: OK (12+ characters)")
    else:
        print("Length: TOO SHORT (less than 12 characters)")

    if strength_assessment['upper_case']:
        print("Upper Case: OK")
    else:
        print("Upper Case: MISSING")

    if strength_assessment['lower_case']:
        print("Lower Case: OK")
    else:
        print("Lower Case: MISSING")

    if strength_assessment['number']:
        print("Number: OK")
    else:
        print("Number: MISSING")

    if strength_assessment['special_char']:
        print("Special Character: OK")
    else:
        print("Special Character: MISSING")

    print("---------------------------")

    score = sum(strength_assessment.values())

    if score == 5:
        print("Password Strength: STRONG")
    elif score >= 3:
        print("Password Strength: FAIR")
    else:
        print("Password Strength: WEAK")

def main():
    password = input("Enter a password: ")
    strength_assessment = assess_password_strength(password)
    provide_feedback(strength_assessment)

if __name__ == "__main__":
    main()