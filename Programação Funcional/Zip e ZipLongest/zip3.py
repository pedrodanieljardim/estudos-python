from itertools import zip_longest, count

indice = count()
cidades = ['SP','BH','SA','RJ','NA']
estados = ['SP','MG','BA','RJ']

# une as listas em uma variável..
estadosUnificados = zip(
    indice,
    cidades,
    estados,
)
for valor in estadosUnificados:
    print(valor)
