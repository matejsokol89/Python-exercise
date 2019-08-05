def find_int():
    find_num = [160, 3, 1719, 19, 11, 13, -21]
    odd_num = 0
    even_num = 0
    count_odd = 0
    count_even = 0

    for i in range(0, len(find_num)):
        if find_num[i] % 2 == 0:
            count_even = count_even + 1
            even_num = find_num[i]

        else:
            count_odd = count_odd + 1
            odd_num = find_num[i]

    if count_even > count_odd:
        print(odd_num)
    else:
        print(even_num)
