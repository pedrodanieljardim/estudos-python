CPF = input()

aux1: int = 10
aux2: int = 11
count1: int = 0
count2: int = 0
i: int = 0
j: int = 0
while i < 12:
    if CPF[i] != '.' and CPF[i] != '-':
        count1 += int(CPF[i]) * aux1
        aux1 -= 1
    i += 1
else:

    aux1 = 11 - (aux1 % 11)
    if aux1 > 9:
        aux1 = 0

    while j < 12:
        if CPF[j] != '.' and CPF[j] != '-':
            if j < 10:
                count2 += int(CPF[j]) * aux2
                aux2 -= 1
            else:
                count2 += int(CPF[j]) * aux2
                count2 += int(CPF[j]) * aux2
                aux2 -= 1
        j += 1
    else:
        aux2 = 11 - (aux2 % 11)
        if aux2 >= 10:
            aux2 = 0

    print("========================================")
    print("    VALIDADE DO CPF ")
    if int(CPF[12]) != aux1 and int(CPF[13]) != aux2:
        print("Status: CPF Inválido...")
    else:
        print("Status: CPF Válido...")

    print("========================================")

