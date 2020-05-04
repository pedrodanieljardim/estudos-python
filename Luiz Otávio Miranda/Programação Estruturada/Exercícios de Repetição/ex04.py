number = input("Digite o valor n:")
i : int = 1
factorial : int = 1

if number.isdigit():
    number = int(number)
    while i <= number:
        factorial *= i
        i += 1
    else:
        print("fatorial de valores de 1 á {}: {}".format(number,factorial))
else:
    print("Entrada inválida..")