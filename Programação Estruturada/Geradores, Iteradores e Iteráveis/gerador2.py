def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g = gera()

print(next(g))
print(next(g))
print(next(g))
