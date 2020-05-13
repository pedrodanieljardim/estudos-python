class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, gastos):
        super(Cliente, self).__init__(nome, idade)
        self.gastos = gastos

    def debito_feito(self):
        print('O Cliente gastou: R$ {:.2f}'.format(self.gastos))

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota_final):
        super(Aluno, self).__init__(nome, idade)
        self.nota_final = nota_final

    def final_semestre(self):
        print('A nota final do semestre do aluno foi: {}'.format(self.nota_final))
