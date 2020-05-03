
age: int = input("Qual é a sua idade?")

if int (age) >= 18:
    print("Pode Entrar!")
else:
    print("Entrada negada!")

height: float = input("Qual é a sua altura?")

if float(height) < 1.00:
    print("Pequenino..")
elif float(height) < 1.50:
    print("Pequeno")
elif float(height) < 1.50:
    print("Manlet...")
else:
    print("Aprovado, Você não é manlet...")