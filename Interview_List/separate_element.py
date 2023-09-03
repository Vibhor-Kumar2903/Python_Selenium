def separate_element(list_a):
    print("=========== SEPARATE_ELEMENT ===========")
    list_x = []
    list_y = []

    for i in range(0, len(list_a)):
        if list_a[i] == 0:
            list_x.append(list_a[i])

    for i in range(0, len(list_a)):
        if list_a[i] != 0:
            list_y.append(list_a[i])

    list_result = list_y + list_x
    print(f"list_result : {list_result}")


given_list = [0, 5, 0, 0, 3, 1, 15, 0, 12]
separate_element(given_list)


