mx = -100000
while True:
    score = int(input())
    if score == -1:
        break
    if score > mx:
        mx = score
print(mx)