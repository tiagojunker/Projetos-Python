import os
import shutil
import datetime

# Guardando dia, mês e ano em variaveis
current_date = datetime.datetime.now()
day = str(current_date.day)
month = str(current_date.month)
year = str(current_date.year)


# Diretório Atual
cwd = os.getcwd()

# Abertura do arquivo txt com o endereço de origem dos documentos
origin_folder = open(fr"{cwd}/origen.txt", "r")
origin = origin_folder.readline()

# Abertura do arquivo txt com o endereço parcial de destino dos documentos
destination_folder = open(fr"{cwd}/destino.txt", "r")
half_destination = destination_folder.readline()

#Destino completo dos arquivos formatando a divisão por dia, mês e ano
destination = fr'{half_destination}{year}\{month}\{year}-{month}-{day}'


# cria o diretório para onde vão os arquivos
try:
    os.mkdir(f'{half_destination}{year}')
except FileExistsError as erro:
    pass

try:
    os.mkdir(f'{half_destination}{year}/{month}')
except FileExistsError as erro:
    pass

try:
    os.mkdir(destination)
except FileExistsError as erro:
    pass

# Varre a página onde estão os arquivos a serem movidos e os move para a pagina destino.
for root, dirs, files in os.walk(origin):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(destination, file)
        shutil.move(old_file_path, new_file_path)