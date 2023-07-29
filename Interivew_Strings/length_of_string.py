# length of a string in python

def length_of_string(string):
    print("====== LENGTH_OF_STRING ======")

    count = 0

    for i in string:
        count += 1

    print(f"length of string : {count}")


given_string = "my name is khan"
length_of_string(given_string)
print(f"By length method : {len(given_string)}")

