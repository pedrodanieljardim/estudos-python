def calculaDivisao (n1,n2):
    if n2 == 0:
        raise ValueError('N2 não pode ser 0!')
    return n1/n2

try:
    print(calculaDivisao(1,0))
except ValueError as error:
    print('Você está tentando dividir um valor por 0!')
    print('LOG: ',error)