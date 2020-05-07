# operadores lógicos com condicionais
# and == && == e
# or == || == ou
# not == ! == não
# in == tem
# not in == não tem

age = input("Qual é a sua idade?")

if int(age) > 0 and int(age) < 5:
    print("Maternal...")

elif int(age) >= 5 and int(age) < 10:
    print("Ensino Fundamental I")

elif int(age) >= 10 and int(age) < 15:
    print("Ensino Fundamental II")

elif int(age) > 15 and int(age) < 18:
    print("Ensino médio....")
else:
    print("Já tá formado...")

name = input("Digite seu nome:")

if 'a' in name or 'e' in name or 'i' in name or 'u' in name or 'o' in name:
    print("Exite pelo menos uma vogal no seu nome!")

if 'a' not in name and 'e' not in name and 'i' not in name and 'u' not in name and 'o' not in name:
    print("Não existe vogal no seu nome!")