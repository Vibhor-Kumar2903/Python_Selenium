# program to count number of vowels using sets in given string

def number_of_vowel(string):
    print("======= NUMBER_OF_VOWEL =======")

    set_vowel = set("aeiouAEIOU")
    vowel_list = []

    string = string.lower()

    for s in string:
        if s in set_vowel:
            vowel_list.append(s)

    print(f"Vowels found : {vowel_list}")
    print(f"number of vowels found : {len(vowel_list)}")


given_string = "welcome2ourcountry34"
number_of_vowel(given_string)
