
hour = input("Digite a hora:")
minute = input("Digite o minuto:")
second = input("Digite o segundo:")

if hour.isdigit() and minute.isdigit() and second.isdigit():
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
        if 0 <= hour <= 11:
            print("Bom Dia!")
            print("Hora atual: {}:{}:{}".format(hour, minute, second))
        elif 12 <= hour <= 17:
            print("Boa Tarde!")
            print("Hora atual: {}:{}:{}".format(hour, minute, second))
        elif 18 <= hour <= 23:
            print("Boa Noite!")
            print("Hora atual: {}:{}:{}".format(hour, minute, second))
    else:
        print("Valores Inválidos para horas...")
else:
    print("Tipos de dados inválidos...")