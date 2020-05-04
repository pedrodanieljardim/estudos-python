name = input("Digite seu nome:")

if len(name) <= 4:
    print("Seu nome é curto....")
elif 5 <= len(name) <= 6:
    print("Seu nome é normal....")
elif len(name) > 6:
    print("Seu nome é muito grande...")