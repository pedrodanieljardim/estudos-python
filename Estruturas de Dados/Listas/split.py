
frase1 = "O rato roeu a roupa, Do rei de Roma. e a rainha, de raiva, roeu o resto."

lista1 = frase1.split(' ')
print(lista1)

for value in lista1:
    print("a palavra {} apareceu {} vezes".format(value,lista1.count(value)))