name = input("Digite seu nome:")
qntWords = len(name)

if int (qntWords) > 4:
    print("O seu nome possui mais que 4 letras...")
else:
    print("O seu nome possui menos que 4 letras...")