def transLista (a):
    listaA = list()
    count: int = 0

    for i in range(0, len(a), 1):
        count += 1
        if count == 10:
            count = 0
            listaA.append('0123456789')
    else:
        print('string a em forma de listaA {}'.format(listaA))
        stringB = '.'.join(listaA)
        return  stringB



string = '0123456789012345678901234567890123456789012345678901234567890123456789'

print('StringB: {}'.format(transLista(string)))
