def validate_password(password):
    # for checking the length condition
    if len(password) > 10:
        return False
    # initial condition Password is not full fill the below condition
    has_upper = False
    has_lower = False
    has_special = False
    has_digit = False
    # checking the above condtion is true or not
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char in '!@#$%^&*(),.?":{}|<>':
            has_special = True
        if char.isdigit():
            has_digit = True

    if not (has_upper and has_lower):
        return False

    if not has_special:
        return False

    if not has_digit:
        return False

    return True


passwords = ["Abcdef!123", "Passw0rd", "SecurePwd@", "Short12$"]
for password in passwords:
    if validate_password(password):
        print("Valid password")
    else:
        print("Not a valid password")