def factorial(num):
    print("=========== Factorial Series ===========")
    print(f"Finding the factorial series of {num}")
    fact = 1
    if num < 0:
        print(f"Enter a valid number")
        print(f"{num} is not valid number to find its factorial")

    if num == 0:
        print(f"Factorial of {num} is 1 (one)")

    if num >= 1:
        for i in range(1, num+1):
            fact = fact*i

        print(f"Factorial of {num} is {fact}")


factorial(5)





