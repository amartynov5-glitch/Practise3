from math import log2
a = int(input())
if log2(a).is_integer():
    print("Верно")
else:
    print("Неверно")