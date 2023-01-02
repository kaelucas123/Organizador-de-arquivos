# Biblioteca que executa funções do sistema.
import os 
# Biblioteca usada para criar o dicinário de arquivos.
import collections
# Biblioteca responsável por aprimorar a função print para algo mais legível.
from pprint import pprint

# Esse programa foi dividido em 3 partes. Na primeira parte nós pegamos o diretório onde vamos trabalhar, na segunda o programa faz uma varredura em todos os arquivos do diretório
# e armazenam seu tipo em um dicionário, por fim, o programa cria as pastas e mandam os arquivos para a pasta designada.

#  Parte reponsável por pegar o diretório de Downloads sem ter que mudar para cada computador.
dowload_path = os.path.join(os.path.expanduser('~'),
    'Downloads'
)

# For responsável por varrer todos os arquivos, aplicando um split para pegar seu tipo.
file_mappings = collections.defaultdict()
for filename in os.listdir(dowload_path):
    file_type = filename.split('.')[-1]
    file_mappings.setdefault(file_type, []).append(filename)

#  Parte responsável por criar as pastas com os tipos de arquivos coletados anteriormente e envia-los para o local determinado.
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(dowload_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_item in folder_items:
        source = os.path.join(dowload_path, folder_item)
        destination = os.path.join(folder_path, folder_item)
        pprint(f'Moving {source} to {destination}')
        os.rename(source, destination)