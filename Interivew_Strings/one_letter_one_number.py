# string has at least one letter and one number

def one_letter_one_number(string):
    print("======== STRING HAS ONE LETTER AND ONE NUMBER =======")

    flag_digit = False
    flag_letter = False

    for letter in string:
        if letter.isalpha():
            flag_digit = True

        if letter.isdigit():
            flag_letter = True

    print(f"Result : {flag_digit and flag_letter}")


given_string_1 = "welcome2ourcountry34"
given_string_2 = "stringwithoutnum"

one_letter_one_number(given_string_1)
one_letter_one_number(given_string_2)
