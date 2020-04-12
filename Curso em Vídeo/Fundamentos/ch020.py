import random

nome =  str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
nome4 = str(input('Aluno 4: '))

lista = [nome,nome2,nome3,nome4]
random.shuffle(lista)
print('Ordem de apresentacao é ')
print(lista)
