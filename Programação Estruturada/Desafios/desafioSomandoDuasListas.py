listaA = [1,2,3,4,5,6,7]
listaB = [1,2,3,4]
listaC = list()

for i in range(0,len(listaB),1):
    listaC.append(listaA[i] + listaB[i])

print('Lista A = {}'.format(listaA))
print('Lista B = {}'.format(listaB))
print('Lista C = {}'.format(listaC))