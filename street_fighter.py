from typing import List


def street_fighter():
    fighters = ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"]

    fighters1: List[List[str]] = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Vegeta", "Picolo", "Gouku", "Krilin", "Gohan", "Friza"],

    ]

    moves = ["right", "right", "left", "right", "left"]
    lista = []

    position = 0
    # f = ""
    save: str

    result_first_row: List[str] = [sub_list for sub_list in fighters1[0]]
    result_second_row = [sub_list for sub_list in fighters1[1]]

    print(result_first_row)
    print(result_second_row)

    # for i in range(0, len(moves)):
    #     # print(moves[i])
    #     if moves[i] == "right":
    #         position = position + 1
    #         print(fighters[position])
    #         lista.append(fighters[position])
    #
    #         if position == len(fighters):
    #             position = 0
    #     elif moves[i] == "left":
    #         position = position - 1
    #         lista.append(fighters[position])
    #         # print(fighters[position])
    #         if position == -1:
    #             position = position
    # print(lista)
    #
