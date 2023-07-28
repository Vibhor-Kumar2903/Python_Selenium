def swapping_without_variable(a, b):
    print("============= SWAPPING NUMBERS ==============")
    print(f"Numbers to swap : a={a} and  b={b}")

    a, b = b, a

    print(f"After swapping : a={a} and b={b}")

    a = a+b
    b = a-b
    a = a-b

    print(f"After swapping again : a={a} and b={b}")


swapping_without_variable(5, 7)

