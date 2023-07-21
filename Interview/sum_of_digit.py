def sum_of_digit(num):
    print("======== SUM_OF_DIGIT ========")
    print(f"Given number is {num}")

    r = 0
    s = 0
    temp = num

    while num > 0:
        r = num % 10
        s = s + r
        num = num // 10

    print(f"Sum of digits in {temp} is {s}")


sum_of_digit(111)
