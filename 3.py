import math
number = int(input())
while number // math.sqrt(number) != math.sqrt(number):
    number = int(input())
print('полный квадрат')