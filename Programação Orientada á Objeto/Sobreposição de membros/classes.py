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

class ClienteVIP(Cliente):
    def __init__(self,nome, idade, gastos, bonus):
        super(ClienteVIP, self).__init__(nome, idade, gastos)
        self.bonus = bonus

    # Override (Sobrecarga em java)
    def debito_feito(self):
        super().debito_feito()
        self.gastos -= (self.gastos *(self.bonus/100))
        print('Desconto VIP de {}%, então o Cliente gastou: R$ {:.2f}'.format(self.bonus, self.gastos))
