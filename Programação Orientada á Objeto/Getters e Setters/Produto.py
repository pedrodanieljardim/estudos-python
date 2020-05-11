class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def getNome(self):
        return self.nome

    @property
    def setNome(self, valor):
        self.nome = valor

    @property
    def getPreco(self):
        return self.preco

    @property
    def setPreco(self,valor):

        if isinstance(valor, str):
            valor = valor.replace('R$','')
            valor = float(valor)

        self.preco = valor

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
        print('Preço com Desconto de {}% : R${:.2f}'.format(percentual, self.preco))

    def mostraProduto(self):
        print('Nome do Produto: {}'.format(self.nome))
        print('Preço do Produto: R${:.2f}'.format(self.preco))
