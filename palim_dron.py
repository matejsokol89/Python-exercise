def palindrome():
    first_order = ""
    back_order = ""
    divide = 0
    word = "perorek"
    lenght: int = int(len(word) / 2 + 1)
    reverse: str = ""

    for i in range(0, lenght):
        first_order = first_order + word[i]
    print(first_order)

    for i in range(len(word), 0, -1):
        reverse = reverse + word[i - 1]
        divide = int(len(reverse) / 2 + 1)

    for j in range(0, divide):
        back_order = back_order + reverse[j]
    print(back_order)
    if first_order == back_order:
        print(True)
    else:
        print(False)
