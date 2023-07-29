# Uppercase Half String

def uppercase_half_string(string):
    print("======= UPPERCASE_HALF_STRING =======")

    half_len = len(string) // 2
    result = ""

    for i in range(len(string)):
        if i < half_len:
            result += string[i].upper()

        else:
            result += string[i]

    print(f"after modification : {result}")


def uppercase_half_string_2(string):

    half_idx = len(string) // 2

    result = string[:half_idx] + string[half_idx:].upper()

    print(f"after modification : {result}")


given_string = "my name is Peter"

uppercase_half_string(given_string)
uppercase_half_string_2(given_string)
