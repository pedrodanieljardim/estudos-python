from itertools import combinations, permutations

listaA = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# função permutations mostra todas possíveis combinações importando a ordem.....
for grupo in permutations(listaA, 2):
    print(grupo)


