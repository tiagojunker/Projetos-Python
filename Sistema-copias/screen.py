import os
from tkinter import *
from tkinter import ttk
root = Tk()

cwd = os.getcwd()

class Application():
    """ # """
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.listar_agendamentos()
        root.mainloop()
      
    # Configuração da tela
    def tela(self):
        """ # """
        self.root.title("TSJ - Copy")
        self.root.configure(background='#1e3743')
        self.root.geometry("750x750")
        self.root.resizable(True, True)
        self.root.maxsize(width="1000", height="1000")
        self.root.minsize(width="400", height="400")

    def frames_da_tela(self):
        """ # """
        self.frame_1 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)
        
        self.frame_2 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        """ # """
        self.bt_salvar = Button(self.frame_1, text='Salvar', command=self.salvar_agendamento,
                             bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.bt_salvar.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.10)


        # self.bt_editar = Button(self.frame_1, text='Editar',
        #                     bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        # self.bt_editar.place(relx=0.14, rely=0.05, relwidth=0.1, relheight=0.10)


        self.lb_nome_agendamento = Label(self.frame_1, text='Nome Do Agendamento',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_nome_agendamento.place(relx=0.02, rely=0.18)


        self.nome_agendamento_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.nome_agendamento_entry.place(relx=0.02, rely=0.26, relwidth=0.45, relheight=0.08)


        self.lb_intervalo = Label(self.frame_1, text='Intervalo (sec)',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_intervalo.place(relx=0.52, rely=0.18)


        self.intervalo_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.intervalo_entry.place(relx=0.52, rely=0.26, relwidth=0.2, relheight=0.08)


        self.lb_origem = Label(self.frame_1, text='Pasta Origem',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_origem.place(relx=0.02, rely=0.36)


        self.origem_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.origem_entry.place(relx=0.02, rely=0.43, relwidth=0.45, relheight=0.08)


        self.lb_destino = Label(self.frame_1, text='Pasta Destino',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_destino.place(relx=0.52, rely=0.36)


        self.destino_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.destino_entry.place(relx=0.52, rely=0.43, relwidth=0.45, relheight=0.08)


        self.bt_deletar = Button(self.frame_1, text='Deletar', command=self.delete_process,
                            bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.bt_deletar.place(relx=0.02, rely=0.65, relwidth=0.1, relheight=0.10)


        self.lb_nome_agendamento_deletar = Label(self.frame_1, text='Nome Do Agendamento a Deletar',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_nome_agendamento_deletar.place(relx=0.02, rely=0.78)


        self.nome_agendamento_deletar_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.nome_agendamento_deletar_entry.place(relx=0.02, rely=0.85, relwidth=0.45, relheight=0.08)


        self.init_services = Button(self.frame_1, text='Iniciar Serviços', command=self.run_script,
                            bg='#00ac58', fg='white', font = ('verdana', 10, 'bold'))
        self.init_services.place(relx=0.77, rely=0.82, relwidth=0.2, relheight=0.10)


        self.stop_services = Button(self.frame_1, text='Parar Serviços', command= self.stop_script,
                            bg='#bd1b20', fg='white', font = ('verdana', 10, 'bold'))
        self.stop_services.place(relx=0.77, rely=0.7, relwidth=0.2, relheight=0.10)

    def lista_frame2(self):
        """ # """
        self.lista_cli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.lista_cli.heading("#0", text='')
        self.lista_cli.heading("#1", text='Nome Agendamento')
        self.lista_cli.heading("#2", text='Origem')
        self.lista_cli.heading("#3", text='Destino')
        self.lista_cli.heading("#4", text='Intervalo')

        self.lista_cli.column('#0', anchor='center', width=1)
        self.lista_cli.column('#1', anchor='center', width=130)
        self.lista_cli.column('#2', anchor='center', width=200)
        self.lista_cli.column('#3', anchor='center', width=200)
        self.lista_cli.column('#4', anchor='center', width=100)

        self.lista_cli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        scroll_bar = Scrollbar (self.lista_cli)
        scroll_bar.pack(side=RIGHT, fill=Y)

    def salvar_agendamento(self):
        """ # """
               
        nome = str(self.nome_agendamento_entry.get())
        origem = str(self.origem_entry.get())
        destino = str(self.destino_entry.get())
        intervalo = str(self.intervalo_entry.get())

        length_caminho =  open(fr"{cwd}/agendamentos.txt", "r", encoding='utf-8')
        length_caminho = length_caminho.readlines()

        if(len(length_caminho) < 3
            and len(nome)       > 1
            and len(origem)     > 1
            and len(destino)    > 1
            and len(intervalo)  > 1):

            caminho =  open(fr"{cwd}/agendamentos.txt", "a", encoding='utf-8') #MUDAR ISSO QUANDO FOR FAZER O EXE retirar /sistema-copias
            caminho.write(f'{nome}_{origem}_{destino}_{intervalo}_ \n')
            caminho.close()
        

        self.nome_agendamento_entry.delete(0, END)
        self.origem_entry.delete(0, END)
        self.destino_entry.delete(0, END)
        self.intervalo_entry.delete(0, END)


        self.listar_agendamentos()

    def listar_agendamentos(self):
        """ # """
        self.lista_cli.delete(*self.lista_cli.get_children())
        caminho =  open(fr"{cwd}/agendamentos.txt", "r", encoding='utf-8')
        caminho = caminho.readlines()
        for i in caminho:
            valores = i.split('_')
            self.lista_cli.insert("", END, values=(valores[0], valores[1], valores[2], valores[3]))

    def delete_process(self):
        """ # """
        line_delete = self.nome_agendamento_deletar_entry.get()

        if(len(line_delete) > 2):
            current_file = open(fr"{cwd}/agendamentos.txt", "r", encoding='utf-8')
            current_file = current_file.readlines()

            preserved_lines = []

            for line in current_file:
                if(line.split('_')[0] != line_delete):
                    preserved_lines.append(line)
            
            if(len(preserved_lines) != 3):
                new_file = open(fr"{cwd}/agendamentos.txt", "w", encoding='utf-8')

                if(len(preserved_lines) == 2):
                    new_file.write(preserved_lines[0])
                    new_file.write(preserved_lines[1])
                    new_file.close()
                    self.listar_agendamentos()

                if(len(preserved_lines) == 1):
                    new_file.write(preserved_lines[0])
                    new_file.close()
                    self.listar_agendamentos()

                if(len(preserved_lines) == 0):
                    new_file.close()
                    self.listar_agendamentos()
                
    def run_script(self):
        try:
            os.system('TASKKILL /F /IM script.exe')
        except:
            pass
        os.popen(fr"{cwd}/script.exe")
    

    def stop_script(self):
        try:
            os.system('TASKKILL /F /IM script.exe')
        except:
            pass 
        # TASKKILL /IM script.exe /T

Application()
# Criar exe tkinter: pyinstaller --onefile --noconsole --windowed screen.py


# Melhorias
# Refatorar
# Gerar um arquivo TXT de Logs
