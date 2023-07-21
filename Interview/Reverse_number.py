def reverse_number(num):
    print("========== REVERSE_NUMBER ==========")
    print(f"Given number {num}")

    r = 0
    s = 0

    while num > 0:
        r = num % 10
        s = (s*10) + r
        num = num // 10

    print(f"Reverse of given number {num} is {s}")


reverse_number(158)
