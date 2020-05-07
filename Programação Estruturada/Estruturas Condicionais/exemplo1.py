
age: int = input("Qual é a sua idade?")
height: float = input("Qual é a sua altura?")

if float(height) < 1.00:
    print("Pequenino..")
elif float(height) < 1.50:
    print("Pequeno")
elif float(height) < 1.50:
    print("Manlet...")
else:
    print("Aprovado, Você não é manlet...")