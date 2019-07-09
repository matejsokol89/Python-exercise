def bubble():
    my_list = [1, 5, 85, 6, 22]

    length = len(my_list) - 1
    sorting = False
    while not sorting:
        sorting = True
        for i in range(length):
            if my_list[i] < my_list[i + 1]:
                sorting = False
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print(my_list)
