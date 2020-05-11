a = int(input("digite um valor:"))
b = int(input("Digite um outro valor:"))

# Funções Lambdas...
# precisam de uma variável para o retorno...
# variável = lambda parâmetro1, parâmetro2: retorno

x = lambda x, y: x * y
y = lambda x, y: x + y
k = lambda x, y: x - y
z = lambda x, y: x / y

print("Adição: {}".format(y(a,b)))
print("Subtração: {}".format(k(a,b)))
print("Multiplicação : {}".format(x(a, b)))
print("Divisão: {}".format(z(a, b)))