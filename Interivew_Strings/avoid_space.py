# Avoid Spaces in string length

def avoid_space(string):
    print("====== LENGTH_OF_STRING ======")

    string = string.replace(" ", "")

    print(f"Length of string without space : {len(string)}")


given_string = "my name is khan"

avoid_space(given_string)

