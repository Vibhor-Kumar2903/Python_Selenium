def perfect_number(num):
    print("======== PERFECT_NUMBER ========")
    print(f"Given number is : {num}")

    s = 0

    for i in range(1, num):
        if num % i == 0:
            s = s + i

    if s == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")


perfect_number(6)
