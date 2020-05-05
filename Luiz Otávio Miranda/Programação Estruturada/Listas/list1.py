
# listas em python

listaA = [1,2,3,4,5,6,"Pedro",True]

#          0   1   2   3   4   5
listaB = ['A','B','C','D','E','F']

print("Lista B: ".format(listaB))

print("Fatiamento de Lista (0 á 3) da Lista B: {}".format(listaB[0:3]))

listaC = [1,2,3]
listaD = [4,5,6]
listaE = listaC+listaD

print("Concatena a lista C e D em E: {}".format(listaE))

print("Lista C: {}".format(listaC))
print("Lista D: {}".format(listaC))

listaC.extend(listaD)
print("Lista C concatenando via Função com a lista D: {}".format(listaC))

listaC.append(7)
listaC.append(8)
listaC.append(9)
listaC.append(10)

print("Lista C com 4 novos valores : {}".format(listaC))

listaC.insert(0, 0)

print("Lista C com 0 na posição 0 da lista : {}".format(listaC))

listaC.pop()

print("Lista C deleta a posição do parâmetro da função (default é o ultimo), logo o dez é removido : {}".format(listaC))

del(listaC[5:10])

print("Lista C com remoção de indice 5 ao 9: {}".format(listaC))

print("Printa o maior valor da lista C: {}".format(max(listaC)))

print("Printa o menor valor da lista C: {}".format(min(listaC)))

# função range cria lista por intervalo

listaF = list(range(1,10))

print("Lista F gerada com a função range: {}".format(listaF))

