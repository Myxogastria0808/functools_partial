def gen():
    yield from [1, 2, 3, 4]

gen_variable = gen()

if __name__ == "__main__":
    #len()は、ジェネレーターに対応していない
    print(len(list(gen()))) # ← 一回、list()にしてからlen()に入れる

    #ジェネレーター関数は、一度動くとメモリを開放する
    #二回目以降はlen()が0になる
    print(len(list(gen_variable)))
    print(len(list(gen_variable)))
    #対策
    #毎回関数で入れる
    print(len(list(gen())))
    print(len(list(gen())))