# ランダムにアルファベットをa桁返す
# 入力値に応じて、b個返すのか決定させる
import random
import think

double_alphabet = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]


# 何桁のアルファベットを返すのか決める
a = int(input("何桁のアルファベットを作成しますか:"))

# 何個返すのか決める
b = int(input("何個も作成しますか："))

# 大文字か小文字が混合か確認
up_low = int(input('大文字の場合は０、小文字の場合は１、混合で作る場合は２を入力してください：'))


with open('all_random.txt', encoding="utf-8", mode="w") as f:

    if up_low <= 1:
        res_list = think.route(a, b, up_low)
        for i in res_list:
            f.write(i)
    else:
        for x in range(b):
            res = ""
            for y in range(a):
                # 2次元配列のどっちにするのか決める
                xy = random.randint(0, 1)
                if xy == 0:
                    ran = random.randint(0, 25)
                    res += double_alphabet[0][ran]
                else:
                    ran = random.randint(0, 25)
                    res += double_alphabet[1][ran]
            res += " "
            print(res, end="")
            f.write(res)