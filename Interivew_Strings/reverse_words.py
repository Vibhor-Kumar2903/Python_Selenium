# Reverse words in a given String in Python

def reverse_words_and_string(string):
    print("========== REVERSE_WORDS ==========")
    print(f"Given string ::  \n{string}")

    string = string.split(" ")
    reverse = ""

    for s in string:
        reverse = reverse + s[::-1] + " "

    print(f"Reverse :: \n{reverse}")


given_string = "my name is khan"

reverse_words_and_string(given_string)


def reverse_words_not_string_1(string):
    print("========== REVERSE_WORDS ==========")
    print(f"Given string ::  \n{string}")

    string = string.split(" ")
    reverse = string[::-1]
    reverse_string = ""

    for w in reverse:
        reverse_string = reverse_string + w + " "

    print(f"Reverse ::  {reverse_string}")


def reverse_words_not_string_2(string):
    print("========== REVERSE_WORDS ==========")
    print(f"Given string ::  \n{string}")

    string = string.split(" ")
    reverse = string[::-1]
    reverse_string = " "

    outcome = reverse_string.join(reverse)

    print(f"Reverse ::  {outcome}")


given_string = "my name is khan"

reverse_words_and_string(given_string)
reverse_words_not_string_1(given_string)
reverse_words_not_string_2(given_string)


