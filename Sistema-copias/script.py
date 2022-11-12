import os
import shutil
import time
import _thread


# Caminho do Diretório do arquivo script.py
cwd = os.getcwd()

def run_service(line):
    """ # """
    while True:
        valores = line.split('_')
        intervalo_copia = valores[3]
        intervalo_copia = int(intervalo_copia)
        origem_arquivos     = valores[1]
        destino_arquivos    = valores[2]

        local = os.listdir(origem_arquivos)
        for data in local:
            shutil.copy2(os.path.join(origem_arquivos, data), destino_arquivos)

        time.sleep(intervalo_copia)

# Abrindo arquivo com os agendamentos
archive = open(fr"{cwd}/agendamentos.txt", "r", encoding='utf-8')
archive = archive.readlines()

for _line in archive:
    _thread.start_new_thread(run_service, (_line,))

while True:
    pass
    
    
        

