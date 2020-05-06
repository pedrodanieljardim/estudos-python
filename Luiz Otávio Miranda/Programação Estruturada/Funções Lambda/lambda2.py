listaA = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 2],
    ['P6', 200],
]
# sort na lista da lista......
print(sorted(listaA,key=lambda i: i[0], reverse=True))
print(listaA)