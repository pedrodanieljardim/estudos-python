import random

nome =  str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
nome4 = str(input('Aluno 4: '))

lista = [nome,nome2,nome3,nome4]
escolhido = random.choices(lista)
print("Quem limpará o quadro será {}".format(escolhido))
