def sum_of_array_elements_1():
    print("============ SUM_OF_ARRAY_ELEMENTS ============")
    list_arr = [2, 3, 7, 5, 11, 2, 0, 1]

    summation_1 = sum(list_arr)
    print(f"sum of list elements : {summation_1}")


sum_of_array_elements_1()


def sum_of_array_elements_2():
    print("============ SUM_OF_ARRAY_ELEMENTS ============")
    list_arr = [2, 3, 7, 5, 11, 2, 0, 1]

    s = 0

    for i in range(len(list_arr)):
        s = s + list_arr[i]

    print(f"sum of list elements : {s}")


sum_of_array_elements_2()


