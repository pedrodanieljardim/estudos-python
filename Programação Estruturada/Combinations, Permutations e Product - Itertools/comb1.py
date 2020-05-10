from itertools import combinations

listaA = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# função combinations mostra todas possíveis combinações.....
for grupo in combinations(listaA, 2):
    print(grupo)


