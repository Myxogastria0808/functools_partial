#イテレータ
class MyIterator(object):
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._i == len(self._numbers):
            raise StopIteration()
        value = self._numbers[self._i]
        self._i += 1
        return value

if __name__ == "__main__":
    my_itreator = MyIterator(10, 20, 30)

    for num in my_itreator:
        print(num)

#イテレータの挙動
# 1. イテレータ化が要求される
# 2. __iter__()メソッドが呼ばれる
# 3. __next__()メソッドは呼ばれる度に新しい値を返す
# 4. __next__()メソッドはもう返す値がないときの呼び出しは、StopIterationという例外をraiseする。

#yieldによる簡略化が可能
def my_generator():
    yield 10
    yield 20
    yield 30

gen = my_generator()

print("gen.__next__()")
gen.__next__()  # 10
gen.__next__()  # 20
gen.__next__()  # 30
gen.__next__()  # StopIteration
