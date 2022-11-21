import os
import shutil
import time
import _thread


# Caminho do Diretório do arquivo script.py
cwd = os.getcwd()

def run_service(line):
    """ # """
    while True:
        values = line.split('_')
        copy_interval = values[3]
        copy_interval = int(copy_interval)
        data_origin   = values[1]
        data_destiny  = values[2]

        try:
            os.system(f'robocopy "{data_origin}" "{data_destiny}" /R:1 /W:1 /MIR')
        except:
            log =  open(fr"{cwd}/assets/log.txt", "a", encoding='utf-8') #MUDAR ISSO QUANDO FOR FAZER O EXE retirar /sistema-copias
            log.write(f'Falha ao copiar arquivos de {data_origin} para {data_destiny} verifique os diretórios \n')
            log.close()

        # local = os.listdir(data_origin)
        # local_to = os.listdir(data_destiny)
        # for data in local:
        #     if(data in local_to):
        #         pass
            
        #     else:
        #         try:
        #             # shutil.copy(os.path.join(data_origin, data), data_destiny)
        #             # log =  open(fr"{cwd}/assets/log.txt", "a", encoding='utf-8') #MUDAR ISSO QUANDO FOR FAZER O EXE retirar /sistema-copias
        #             # log.write(f'Arquivo {data} copiado com Sucesso \n')
        #             # log.close()
        #         except:
        #             print('Não copiado')

        time.sleep(copy_interval)

# Abrindo arquivo com os agendamentos
archive = open(fr"{cwd}/assets/agendamentos.txt", "r", encoding='utf-8')
archive = archive.readlines()

for _line in archive:
    _thread.start_new_thread(run_service, (_line,))

while True:
    pass
    