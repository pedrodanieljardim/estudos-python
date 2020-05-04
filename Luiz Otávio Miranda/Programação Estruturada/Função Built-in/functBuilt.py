num1 = input("Digite um número:")
num2 = input("Digite outro número:")

if num1.isdigit() and num2.isdigit():
    # função isdigit retorna valor booleano indicando se a string digitada é um dígito
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    print("A soma entre {} e {} é {}".format(num1, num2, sum))
else:
    print("Aconteceu um erro...")
