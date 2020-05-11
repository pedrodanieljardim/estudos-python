print("==========================================================")

try:
    print('Valor inteiro para A: ')
    a = int(input())
    print('Valor inteiro para B: ')
    b = int(input())
    c = b/a
except ZeroDivisionError:
    print('ERRO! Divisão feita por zero é Impossível!')
except ValueError:
    print('ERRO! Entrada feita com valor não permitido!')
else:
    print('Operação Feita com sucesso: {}/{} = {}'.format(a,b,c))
finally:
    print('Esse bloco será executado independe se ocorre ou não ocorre exceção...')
    print("==========================================================")

