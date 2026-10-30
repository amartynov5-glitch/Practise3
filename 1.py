n = []
c = 0
for i in range(1, 1000):
    if i % 17 == 0:
        c+=1
        n.append(i)
print(*n)
print(str(c))