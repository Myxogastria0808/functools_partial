#functools.partial()を使おう

import functools

def add(x, y):
    return x + y

add_1 = functools.partial(add, 1)

print(add_1(2))

add_2 = functools.partial(add, y=0)

print(add_2(2))