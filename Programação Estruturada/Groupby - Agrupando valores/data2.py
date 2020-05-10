from itertools import groupby

alunos = [
    {'nome':'Luiz','nota':'A'},
    {'nome':'Letícia','nota':'B'},
    {'nome':'Fabrício','nota':'C'},
    {'nome':'Rosemary','nota':'A'},
    {'nome':'Joana','nota':'B'},
    {'nome':'João','nota':'C'},
    {'nome':'Eduardo','nota':'A'},
    {'nome':'André','nota':'B'},
    {'nome':'Anderson','nota':'C'},
    {'nome':'José','nota':'A'},
]

ordena=  lambda item: item['nota']
alunos.sort(key = ordena)
# ordenados alunos pela nota
print(alunos)
alunosAgrupados = groupby(alunos, ordena)

for agrupamento, valoresAgrupados in alunosAgrupados:
    print('\n Agrupamento: {}'.format(agrupamento))
    quantidade = len(list(valoresAgrupados))
    print('{} alunos tiraram a nota {}'.format(quantidade, agrupamento))