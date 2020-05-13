from classes import *

c1 = Cliente('Luiz', 45, 800)
c2 = ClienteVIP('Pedro', 22, 1200, 12)

print('===============================================')
print('Cliente: {} '.format(c1.nome))
print('Idade: {}'.format(c1.idade))
c1.debito_feito()
print('===============================================')
print('Cliente VIP: {} '.format(c2.nome))
print('Idade: {}'.format(c2.idade))
c2.debito_feito()
print('===============================================')
