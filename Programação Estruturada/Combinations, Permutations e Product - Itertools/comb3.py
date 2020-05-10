from itertools import combinations, permutations, product

listaA = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# função product mostra todas possíveis combinações importando a ordem e repete valores únicos...
for grupo in product(listaA, repeat=2):
    print(grupo)


