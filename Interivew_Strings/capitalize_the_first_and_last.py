# capitalize the first and last character

def capitalize(string):
    print("======== CAPITALIZE THE FIRST AND LAST CHARACTER =======")

    word = string.split(" ")

    caps = []

    for w in word:
        x = w[0].upper() + w[1:-1] + w[-1].upper()
        caps.append(x)

    result = " ".join(caps)
    print(f"Result : {result}")


given_string = "my name is manoj"
capitalize(given_string)
