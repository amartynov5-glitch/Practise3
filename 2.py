a = input()
result = ''.join(a[i] for i in range(2, len(a), 3))
print(result)