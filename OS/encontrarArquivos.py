import os


def convert_size(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        size = base
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'

    size = round(size, 2)
    return f'{size}{text}'


search_directory = input()
search_word = input()
count = 0

for root, directory, archives in os.walk(search_directory):
    for archive in archives:
        if search_word in archive:
            try:
                count += 1
                complete_directory = os.path.join(root, archive)
                archive_name, archive_ext = os.path.splitext(complete_directory)
                print(archive_name, archive_ext)
                archive_size = os.path.getsize(complete_directory)
                print()
                print('Encontrei o Arquivo:', archive)
                print('Caminho: ', complete_directory)
                print('Nome: ', archive_name)
                print('Extensão: ', archive_ext)
                print('Tamanho: ', archive_size)
                print('Tamanho Formatado: ', convert_size(archive_size))

            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print('{} arquivo(s) encontrado(s)'.format(count))
