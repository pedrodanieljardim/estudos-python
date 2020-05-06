
tuplaA = (1, 2, 3, 4, 5)

print('Tupla A: {}'.format(tuplaA))
print('Tipo: {}'.format(type(tuplaA)))
print("==========================================")

tuplaB = (6, 7, 8, 9, 10)
print('Tupla B: {}'.format(tuplaB))
print('Tipo: {}'.format(type(tuplaB)))

print("==========================================")

print('Soma de tupla A e B:')
# concatena listas....
tuplaC = tuplaA + tuplaB
print('Tupla C: {}'.format(tuplaC))
print('Tipo: {}'.format(type(tuplaC)))

print("==========================================")

print('Operação com tupla')
tuplaD = tuplaA * 2
# Multiplicação repete a tupla n vezes...
print('Tupla D: {}'.format(tuplaD))
print('Tipo: {}'.format(type(tuplaD)))

print("==========================================")

print('Transformando a tupla em lista...')

tuplaA = list(tuplaA)
tuplaA[1] = 2000

print('Tupla A: {}'.format(tuplaA))
print('Tipo: {}'.format(type(tuplaA)))