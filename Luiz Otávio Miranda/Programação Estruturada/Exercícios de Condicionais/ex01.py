number = input("Digite um número inteiro:")

if number.isdigit():
    number = int (number)
    if number % 2 == 0:
        print("o valor {} é par!".format(number))
    else:
        print("o valor {} não é par!".format(number))
else:
    print("O valor digitado não é valido!")