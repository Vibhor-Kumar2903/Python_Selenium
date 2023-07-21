def number_of_digit(num):
    print("========== NUMBER_OF_DIGIT =========")
    print(f"Given number : {num}")

    temp = num
    r = 0
    count = 0

    while num > 0:
        r = num % 10
        count += 1
        num = num // 10

    print(f"Number of digits in {temp} is : {count}")


number_of_digit(20000)
