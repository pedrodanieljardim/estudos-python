cliente = {
    'Cliente1':{
        'Nome': 'Pedro',
        'Sobrenome': 'Daniel',
    },
    'Cliente2':{
        'Nome': 'Luiz',
        'Sobrenome': 'Otávio',
    },
    'Cliente3':{
        'Nome': 'João',
        'Sobrenome': 'Moreira',
    },
}

for clienteK, clienteV in cliente.items():
    print('======================================')
    print('Exibindo clientes: {}'.format(clienteK))
    for dadosK, dadosV in clienteV.items():
        print(f'\t {dadosK} = {dadosV}')