# Program to accept the strings which contains all vowels

def contain_vowel_1(string):
    print("======= STRINGS CONTAINS ALL VOWELS =======")

    if len(set(string.lower()).intersection("aeiou")) == 5:
        return "Acceptable"

    else:
        return "Not Acceptable"


given_string = "welcome2ourcountry34aiu"
print(contain_vowel_1(given_string))
