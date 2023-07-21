def palindrome_number(num):
    print("========== PALINDROME NUMBER ==========")
    print(f"Given number {num}")

    r = 0
    s = 0
    temp = num

    while num > 0:
        r = num % 10
        s = (s*10) + r
        num = num // 10

    if temp == s:
        print(f"{temp} is a palindrome number")

    else:
        print(f"{temp} is not a palindrome number")


palindrome_number(12221)
