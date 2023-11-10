x = [1, 2, 3, 4, 5]

#ジェネレーター式
#内包表記を()で囲めばよい
gen = (i**2 for i in x)
print(gen)
print(list(gen))