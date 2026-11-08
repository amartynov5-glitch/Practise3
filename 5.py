n = int(input())
z = [i**3 for i in range(1, n+1) if i**3 < n]
print(*z)
