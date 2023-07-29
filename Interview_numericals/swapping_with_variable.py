def swapping_with_variable(a, b):
    print("============= SWAPPING NUMBERS ==============")
    print(f"Numbers to swap : a={a} and  b={b}")

    temp = a
    a = b
    b = temp

    print(f"After swapping : a={a} and b={b}")


swapping_with_variable(5, 7)
