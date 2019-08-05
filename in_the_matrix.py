from typing import List

a: List[List[int]] = [
    [5, 1, 7],
    [1, 1, 7],
    [1, 7, 7]
]


def sum_all_seven():
    sum_up: int = 0
    for i in range(0, len(a)):
        for index in a[i]:
            if index == 7:
                sum_up: int = sum_up + index
    print(sum_up)


def sum_specific_seven():
    flat_list: List[int] = []
    sum_up_seven: int = 0
    for i in range(0, len(a)):
        for res in a[i]:
            flat_list.append(res)
    for i in range(0, len(flat_list)):
        if flat_list[i] == 1 and flat_list[i + 1] == 7:
            sum_up_seven: int = sum_up_seven + flat_list[i + 1]
    print(sum_up_seven)
