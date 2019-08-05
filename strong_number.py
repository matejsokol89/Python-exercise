import math
from typing import List


# here just pass the number for now is 145, but you can type any number for test case.
def strong_num():
    number: int = 145
    sum_up: int = 0
    split_number: List[int] = [int(d) for d in str(number)]
    # here is logic for splitting number it should parse int to str
    # to get each element as char then append it to list as 1,4,5
    # another way to solve this step:
    # list_num = []
    # for str_new in str(number):
    #     list_num.append(int(str_new))
    # print(list_num)

    for i in range(0, len(split_number)):
        result: int = math.factorial(split_number[i])
        sum_up: int = sum_up + result
        # for loop the list split_number, and pass each element into python's math.factorial function
        # sum it up at the end
    if number == sum_up:
        print("STRONG!!!!")
    else:
        print("Not Strong !!")
    # if else statement that checks if given number is equal to sum
