def prime_number_in_a_range(r1, r2):
    print("======== PRIME NUMBER ========")
    print(f"Search for prime numbers between {r1} and {r2}")

    prime_list = []
    for num in range(r1, r2+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1

        if count == 2:
            prime_list.append(num)

    print(prime_list)


prime_number_in_a_range(1, 100)

