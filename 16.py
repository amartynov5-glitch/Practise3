n = int(input())
for number in range(1, n+1):

    suma = 0
    for i in range(1, (number//2)+1):
        if number % i == 0:
            suma += i
            #print(i)
    if suma == number:
        print(number)
