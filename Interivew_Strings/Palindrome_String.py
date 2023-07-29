# Python program to check whether the string is Symmetrical or Palindrome

def palindrome_string(string):
    print("======= PALINDROME_STRING =======")
    print(f"Given String is ::   {string}")

    reverse = string[::-1]

    print(f"Reverse of given string is ::   {reverse}")

    if string == reverse:
        print("String is palindrome.")
    else:
        print("String is not a palindrome.")


palindrome_string("mom")


