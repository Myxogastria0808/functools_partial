#yield from文
#二重ループの略記ができる

def unko_gen():
    for i in [(1,2,3), ('A', 'B', 'C')]:
        print('--------')
        for iter in i:
            yield iter

def gen():
    for i in [(1,2,3), ('A', 'B', 'C')]:
        print('--------')
        yield from i

if __name__ == "__main__":
    print('unko_gen()')
    for num in unko_gen():
        print(num)
    print('gen()')
    for num in gen():
        print(num)