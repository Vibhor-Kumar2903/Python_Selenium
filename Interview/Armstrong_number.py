def armstrong_number(num):
    print("========= ARMSTRONG_NUMBER =========")
    print(f"given number : {num}")

    temp = num
    r = 0
    s = 0

    while num > 0:
        r = num % 10
        s = (r*r*r) + s
        num = num // 10

    if temp == s:
        print(f"Sum of cubes : {s}")
        print(f"{temp} is armstrong number")
    else:
        print(f"{temp} is not a armstrong number")


armstrong_number(153)
