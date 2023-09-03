# Remove i’th character from string in Python

def remove_letters(string):

    removed_str = string.translate({ord(i): None for i in "ain"})
    print(f"removed_str :: {removed_str}")


given_string = "my name is khan"

remove_letters(given_string)

