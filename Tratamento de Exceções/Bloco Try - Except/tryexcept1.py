print("==========================================================")
try:
    print(a)
    # sintaxe - captura e trata (try e except)
except NameError as erro:
    # trata exceção de variável não instanciada..
    print('Aconteceu uma Exceção do tipo: {}'.format(erro))
except Exception as erro:
    print('Ocorreu um erro inesperado ')
else:
    print('Não houve exceções!!!')
finally:
    print('Esse bloco será executado independe se ocorre ou não ocorre exceção...')
    print("==========================================================")


print('Continuando o fluxo do código..')
print("==========================================================")

try:
    b = []
    print(b[2])
except (IndexError,KeyError) as erro:
    print('Aconteceu uma Exceção do tipo: {}'.format(erro))
finally:
    print('Esse bloco será executado independe se ocorre ou não ocorre exceção...')
    print("==========================================================")
