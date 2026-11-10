x = int(input())
count = 0
for a in range(1, int(x**0.5)):
    b2 = x - a**2
    if (b2**0.5).is_integer():
        count+=1
print(count)
