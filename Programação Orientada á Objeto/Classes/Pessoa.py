class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def estaComendo(self):
        if self.comendo == True:
            print('{} está comendo !!!'.format(self.nome))
        else:
            print('{} não está comendo !!!!!!'.format(self.nome))
