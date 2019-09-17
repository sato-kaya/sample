# ランダムにアルファベットをa桁返す
# 入力値に応じて、b個返すのか決定させる
from random import randint


# アルファベットのリスト
low_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
up_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 何桁のアルファベットを返すのか決める
a = int(input("何桁のアルファベットを作成しますか:"))

# 何個返すのか決める
b = int(input("何個も作成しますか："))

# 大文字か小文字が混合か確認
up_low = int(input('大文字の場合は０、小文字の場合は１、混合で作る場合は２を入力してください：'))

if up_low == 0:
    for x in b:
        res = ''
        for y in a:
            res += up_alphabet[randint(26)]
        print(res, end=" ")
elif up_low == 1:
    for x in b:
        res = ''
        for y in a:
            res += up_alphabet[randint(26)]
        print(res, end=" ")
else:
    for x in b:
        res = ""
        for y in a: