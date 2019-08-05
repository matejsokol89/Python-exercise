def odd_num():
    odd_list = []
    number = 15
    for i in range(0, number):
        if i % 2 == 1:
            odd_list.append(i)
    print(len(odd_list))
