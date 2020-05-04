n = input("Digite um valor n:")

if n.isdigit():
    i:int = 0
    n = int(n)
    while i <= n:
        print(i)
        i += 1
    else:
        print("Contagem Terminada...")
else:
    print("{} não é qualificado como dígito...".format(n))