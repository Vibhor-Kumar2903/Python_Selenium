import string


def validate_password(password):
    has_upper = False
    has_lower = False
    has_special_char = False
    has_digit = False

    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in string.punctuation:
            has_special_char = True

    if not (has_upper and has_lower):
        return False

    if not has_special_char:
        return False

    if not has_digit:
        return False

    return True


def alphanumeric_and_spacial_character():
    print("========= ALPHANUMERIC_AND_SPACIAL_CHARACTER =========")

    password_list = ["Abcdef!123", "Passw0rd", "SecurePwd@", "Short12$", 'name@123', 'name12345', 'Name@#111', '@#$123']
    for pas in password_list:
        if validate_password(pas):
            print(f"{pas} is ACCEPTABLE")
        else:
            print(f"{pas} is NOT acceptable")


alphanumeric_and_spacial_character()
