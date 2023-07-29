# program to print even length words in a string

def even_length_word(string):
    print("========= EVEN_LENGTH_WORD ========")

    str_list = string.split(" ")

    for s in str_list:
        if len(s) % 2 == 0:
            print(s)


given_string = "my name is manoj"
even_length_word(given_string)
