# Count the Number of matching characters in a pair of string
def matching_characters(string_1, string_2):
    print("======= COUNT MATCHING CHARACTERS =======")

    set_string_1 = set(string_1)
    set_string_2 = set(string_2)

    matched = set_string_1 & set_string_2

    print(f"number of matched characters are : {len(matched)}")


given_string_1 = "welcome2ourcountry34"
given_string_2 = "stringwithoutnum"

matching_characters(given_string_1, given_string_2)

