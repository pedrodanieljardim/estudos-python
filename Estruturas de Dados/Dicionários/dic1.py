d1 = {'chave1':'valor da chave'}
print('Dicionário d1: {}'.format(d1))

d1['chave2'] = 'valor da chave 2'
print('Dicionário d1: {}'.format(d1))

print('======================================================')

d2 = dict(chave1=1, chave2=2, chave3=3)
print('Dicionário D2: {}'.format(d2))
d2['chave4'] = 4
print('Dicionário D2: {}'.format(d2))

print('======================================================')
d3 = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print('Dicionário D3: {}'.format(d3))
print('Posição 1 do dicionário d3: {}'.format(d3[1]))
print('Posição 2 do dicionário d3: {}'.format(d3[2]))
print('Posição 3 do dicionário d3: {}'.format(d3[3]))
print('Posição 4 do dicionário d3: {}'.format(d3[4]))

print('======================================================')

d5 = {
    'str': 'valor',
    123: 'valor',
    (1, 2, 3, 4): 'Tupla',
}
print('Dicionário D5: {}'.format(d5))

if 'str' in d5:
    print('Existe a chave str no dicionário d5')
else:
    print('Não existe a chave str no dicionário d5')

if 'A' not in d5:
    print('Não existe a chave A no dicionário d5')
else:
    print('Existe a chave A no dicionário d5')

print('======================================================')

d6 = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print('Dicionário D6: {}'.format(d6))
print('Posição 1 do dicionário d6: {}'.format(d6[1]))
print('Posição 2 do dicionário d6: {}'.format(d6[2]))
print('Posição 3 do dicionário d6: {}'.format(d6[3]))
print('Posição 4 do dicionário d6: {}'.format(d6[4]))

del d6[1]
d6.update({5: 'E'})
print('Dicionário D6: {}'.format(d6))
print('Existe a chave 2 no dicionário d6? {}'.format(2 in d6.keys()))
print('Existe o valor B no dicionário d6? {}'.format('B' in d6.values()))
print('Tamanho do dicionário d6: {}'.format(len(d6)))

print('======================================================')
d7 = {'ChaveA': 1, 'ChaveB': 2, 'ChaveC': 3, 'ChaveD': 4, 'ChaveE': 5}
print('Dicionário D7: {}'.format(d7))

print('Printando chaves com forEach:')
print('------------------------------------------------------')
for k in d7:
    print(k)
else:
    print('------------------------------------------------------')

print('Printando valores com forEach:')
print('------------------------------------------------------')
for k in d7.values():
    print(k)
else:
    print('------------------------------------------------------')

print('Printando chaves e valores com forEach:')
print('------------------------------------------------------')

for k in d7.items():
    print('Chave: {} & Valor: {}'.format(k[0], k[1]))
else:
    print('------------------------------------------------------')

