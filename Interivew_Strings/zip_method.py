def zip_method():

    list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    list_b = [1, 2, 3, 4, 5, 6, 7]
    list_c = ['!', '@', '#', '$', '%', '^', '&']

    x = zip(list_a, list_b, list_c)

    print(f"After zip : \n {list(x)}")


zip_method()
