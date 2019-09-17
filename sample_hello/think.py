import random

# アルファベットのリスト
double_alphabet = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]


def route(a, b, x):
    res_list = []
    for qe in range(b):
        res = ''
        for we in range(a):
            ran = random.randint(0, 25)
            res += double_alphabet[x][ran]
        res += " "
        res_list.append(res)

    return res_list


