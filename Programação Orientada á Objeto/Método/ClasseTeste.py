from Pessoa import Pessoa

print("==========================================================")

p1 = Pessoa('Pedro',21)

print('Nome: {}'.format(p1.nome))
print('Idade: {}'.format(p1.idade))
p1.get_ano_nascimento()

print("==========================================================")

p2 = Pessoa.criaPessoa_ano_nascimento('Luiz', 1987)
print('Nome: {}'.format(p2.nome))
print('Idade: {}'.format(p2.idade))
p2.get_ano_nascimento()

print("==========================================================")

p3 = Pessoa('Joel',78)

print('Nome: {}'.format(p3.nome))
print('Idade: {}'.format(p3.idade))
p3.get_ano_nascimento()

print("==========================================================")
