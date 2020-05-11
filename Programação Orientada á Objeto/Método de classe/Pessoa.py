class Pessoa:
    anoAtual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print('Ano de Nascimento: {}'.format(self.anoAtual - self.idade))

    @classmethod
    def criaPessoa_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.anoAtual - ano_nascimento
        return cls(nome, idade)
