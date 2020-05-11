def converteValor(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    n = converteValor(input('Digite um número:'))

    if n is not None:
        print(n * 5)
    else:
        print('n não é número')
