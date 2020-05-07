import math

adjacent = float(input('Digite o valor do cateto adjacente: '))
opposite = float(input('Digite o valor do cateto oposto:'))

hipotenusa = math.sqrt(math.pow(adjacent,2)+math.pow(opposite,2))

print('O tamanho do hipotenusa é {:.2f}'.format(hipotenusa))