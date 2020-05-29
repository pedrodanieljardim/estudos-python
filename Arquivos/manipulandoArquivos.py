# manipulando arquivos

# abrir um arquivo para escrita
arq = open('arquivo.txt', 'w')

# mensagem que será escrita no arquivo
msg = '''Esse eh um exemplo
de mensagem que irei escrever
no arquivo
'''

# escrevendo no arquivo
arq.write(msg)

# fechando o arquivo
arq.close()

# abrindo o arquivo para leitura
arq = open('arquivo.txt', 'r')

# imprimindo o texto do arquivo
print(''.join(linha for linha in arq.readlines()))

# fechando o arquivo
arq.close()