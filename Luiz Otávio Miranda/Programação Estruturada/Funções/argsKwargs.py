def func(*args):
    print("Parâmetros: {}".format(args))
    print("Tamanho do Args: {}".format(len(args)))


def func2(*args, **kwargs):
    print("Parâmetros: {}".format(args))
    print("Tamanho do Args: {}".format(len(args)))
    print(kwargs['nome'], kwargs['SobreNome'])
    nome = kwargs.get('Nome')
    print("Nome = {}".format(nome))


# args é basicamente uma tupla, que reconhece infinitos parâmetros
print("===========================================")
func(1, 2, 3, 4, 5)
print("===========================================")
func('a', 'b', 'c', 'd')
print("===========================================")
func(True, True, False, False)
print("===========================================")
lista = [0, 1, 2, 3, 4, 5]
func(lista)
print("===========================================")
# keywargs são para parâmetros chaves, argumentos nomeados
func2(lista, Nome='Pedro', SobreNome='Daniel')
