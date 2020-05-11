from itertools import zip_longest, count

indice = count()
cidades = ['SP','BH','SA','RJ','NA']
estados = ['SP','MG','BA','RJ']

# une as listas em uma variável..
estadosUnificados = zip_longest(
    indice,
    cidades,
    estados,
    fillvalue='Estado'
)
for indice, estado, cidade in estadosUnificados:
    print(indice, estado, cidade)
