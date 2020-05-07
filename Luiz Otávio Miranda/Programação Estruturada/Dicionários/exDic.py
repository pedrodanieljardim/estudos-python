perguntas = {
    'Pergunta 1 ':{
        'pergunta': 'Quanto é  2+2?',
        'respostas':{'a':'1', 'b':'4', 'c':'5'},
        'respostaCerta': 'b'},
    'Pergunta 2':{
        'pergunta': 'Quanto é  3*2?',
        'respostas':{'a': '4', 'b': '10', 'c': '6'},
        'respostaCerta': 'c'},
    'Pergunta 3':{
        'pergunta': 'Quanto é  4/2?',
        'respostas':{'a': '2', 'b': '1', 'c': '8'},
        'respostaCerta': 'a'},
    'Pergunta 4':{
        'pergunta': 'Quanto é  25^1/2?',
        'respostas':{'a': '25', 'b': '12', 'c': '5'},
        'respostaCerta': 'c'},
    }

count: int = 0

for chavePergunta, chaveResposta in perguntas.items():
    print("\n")
    print(f'{chavePergunta} : {chaveResposta["pergunta"]}')
    print('Respostas: ')
    for rK, rV in chaveResposta['respostas'].items():
        print(f'[{rK}] : {rV}')

    respostaUsuario = input("Sua Resposta:")
    if respostaUsuario == chaveResposta['respostaCerta']:
        print('Resposta Certa!')
        count += 1
    else:
        print('Resposta Errada!')
else:
    print('Quantidade de acertos: {}'.format(count))