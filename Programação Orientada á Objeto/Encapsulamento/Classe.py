
 # Em python, privado (__) e protected (_)
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserirCliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listaCliente(self):
        for id, nome in self.__dados['clientes'].items( ):
            print(id,nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]