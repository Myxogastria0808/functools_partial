#イテレーターの生成器
#for文で動くとき、次の要素が求められるたびにメモリを確保する。

def gen_1():
    yield "Hello"
    yield "World"
    yield "!"

if __name__ == "__main__":
    #イテラブルなobject
    print(gen_1())
    #実際の使い方
    #戻り値は、ジェネレータイテレータ
    for i in gen_1():
        print(i)