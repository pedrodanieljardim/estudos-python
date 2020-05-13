d1 = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D'
}

print('Dicionário d1: {}'.format(d1))
d1.pop(2)
print('Dicionário d1: {}'.format(d1))

d2 = {
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H'
}

d1.update(d2)
print('Dicionário d1: {}'.format(d1))
