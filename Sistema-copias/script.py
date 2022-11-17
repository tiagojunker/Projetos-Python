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
        local_to = os.listdir(destino_arquivos)
        for data in local:
            if(data in local_to):
                pass
            
            else:
                try:
                    shutil.copy(os.path.join(origem_arquivos, data), destino_arquivos)
                    log =  open(fr"{cwd}/log.txt", "a", encoding='utf-8') #MUDAR ISSO QUANDO FOR FAZER O EXE retirar /sistema-copias
                    log.write(f'Arquivo {data} copiado com Sucesso \n')
                    log.close()
                except:
                    print('Não copiado')

        time.sleep(intervalo_copia)

# Abrindo arquivo com os agendamentos
archive = open(fr"{cwd}/agendamentos.txt", "r", encoding='utf-8')
archive = archive.readlines()

for _line in archive:
    _thread.start_new_thread(run_service, (_line,))

while True:
    pass
    
    
        

