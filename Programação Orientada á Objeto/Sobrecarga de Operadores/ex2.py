class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, other):
        preco_a = self.preco
        preco_b = other.preco
        return Produto('Produto Somado',preco_a+preco_b)


produtoA = Produto('Leite',4.50)
produtoB = Produto('Carne', 10.90)

produtoC = produtoA + produtoB

print('{}'.format(produtoC.nome))
print('R$ {:.2f}'.format(produtoC.preco))