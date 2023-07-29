def prime_number(num):
    print("======== PRIME NUMBER ========")
    print(f"verifying that given number {num} is prime or not ")

    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


prime_number(97)

