prevtemp = float(input())
count = 0
while True:
    currentemp = float(input())
    if currentemp == 0:
        break
    if currentemp < prevtemp:
        count += 1
    else:
        continue
print(count)