while True:
    print("Введите число: ", end="")
    userinput = input()
    if userinput.isdigit():
        number = int(userinput)
        break
    else:
        print("Ошибка. Попробуйте еще раз. ", end="")

print(f"Введено целое число: {number}")