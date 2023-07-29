def fibonacci(num):
    print("======== Fibonacci Sequence =========")
    print("Fibonacci sequence of {} is :".format(num))

    fib = 0
    summ = 1

    for i in range(0, num+1):
        print(f"{fib} ", end="")
        term = fib + summ
        fib = summ
        summ = term


fibonacci(10)
