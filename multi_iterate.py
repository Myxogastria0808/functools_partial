#死ぬパターン
def my_generator(n):
    yield n + 1
    yield n + 2

gen = my_generator(10)

print('first time:')
for n in gen:
    print(n)
print('second time:')
for n in gen:
    print(n)


#繰り返し使いたい
import functools


class ReiteratableWrapper(object):
    def __init__(self, f):
        self._f = f
        #毎回リセットされる
    def __iter__(self):
        return self._f()

def my_generator(n):
    yield n + 1
    yield n + 2

f = functools.partial(my_generator, 10)

gen = ReiteratableWrapper(f)

print('first time:')
for n in gen:
    print(n)
print('second time:')
for n in gen:
    print(n)