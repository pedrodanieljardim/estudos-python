number = input("Digite o valor n:")
i : int = 0
summation : int = 0

if number.isdigit():
    number = int(number)
    while i <= number:
        summation += i
        i += 1
    else:
        print("Soma de valores de 0 á {}: {}".format(number,summation))
else:
    print("Entrada inválida..")