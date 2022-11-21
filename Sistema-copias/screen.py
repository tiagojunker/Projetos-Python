import os
from tkinter import *
from tkinter import ttk
root = Tk()

cwd = os.getcwd()

class Application():
    """ # """
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_of_screen()
        self.frame1_widgets()
        self.frame2_list()
        self.show_tasks()
        root.mainloop()
      
    # Configuração da tela
    def screen(self):
        """ # """
        self.root.title("TSJ - Copy")
        self.root.configure(background='#1e3743')
        self.root.geometry("750x750")
        self.root.resizable(True, True)
        self.root.maxsize(width="1000", height="1000")
        self.root.minsize(width="400", height="400")

    def frames_of_screen(self):
        """ # """
        self.frame_1 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)
        
        self.frame_2 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

    def frame1_widgets(self):
        """ # """
        self.save_btn = Button(self.frame_1, text='Salvar', command=self.save_task,
                             bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.save_btn.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.10)


        # self.bt_editar = Button(self.frame_1, text='Editar',
        #                     bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        # self.bt_editar.place(relx=0.14, rely=0.05, relwidth=0.1, relheight=0.10)


        self.name_task_label = Label(self.frame_1, text='Nome Do Agendamento',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.name_task_label.place(relx=0.02, rely=0.18)


        self.name_task_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.name_task_entry.place(relx=0.02, rely=0.26, relwidth=0.45, relheight=0.08)


        self.interval_label = Label(self.frame_1, text='Intervalo (sec)',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.interval_label.place(relx=0.52, rely=0.18)


        self.interval_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.interval_entry.place(relx=0.52, rely=0.26, relwidth=0.2, relheight=0.08)


        self.origin_label = Label(self.frame_1, text='Pasta Origem',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.origin_label.place(relx=0.02, rely=0.36)


        self.origin_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.origin_entry.place(relx=0.02, rely=0.43, relwidth=0.45, relheight=0.08)


        self.destiny_label = Label(self.frame_1, text='Pasta Destino',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.destiny_label.place(relx=0.52, rely=0.36)


        self.destiny_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.destiny_entry.place(relx=0.52, rely=0.43, relwidth=0.45, relheight=0.08)


        self.delete_btn = Button(self.frame_1, text='Deletar', command=self.delete_task,
                            bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.delete_btn.place(relx=0.02, rely=0.65, relwidth=0.1, relheight=0.10)


        self.delete_name_task_label = Label(self.frame_1, text='Nome Do Agendamento a Deletar',
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.delete_name_task_label.place(relx=0.02, rely=0.78)


        self.name_task_delete_entry = Entry(self.frame_1,
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.name_task_delete_entry.place(relx=0.02, rely=0.85, relwidth=0.45, relheight=0.08)


        self.init_services = Button(self.frame_1, text='Iniciar Serviços', command=self.start_program,
                            bg='#00ac58', fg='white', font = ('verdana', 10, 'bold'))
        self.init_services.place(relx=0.77, rely=0.82, relwidth=0.2, relheight=0.10)


        self.stop_services = Button(self.frame_1, text='Parar Serviços', command= self.Stop_program,
                            bg='#bd1b20', fg='white', font = ('verdana', 10, 'bold'))
        self.stop_services.place(relx=0.77, rely=0.7, relwidth=0.2, relheight=0.10)

    def frame2_list(self):
        """ # """
        self.cli_list = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.cli_list.heading("#0", text='')
        self.cli_list.heading("#1", text='Nome Agendamento')
        self.cli_list.heading("#2", text='Origem')
        self.cli_list.heading("#3", text='Destino')
        self.cli_list.heading("#4", text='Intervalo')

        self.cli_list.column('#0', anchor='center', width=1)
        self.cli_list.column('#1', anchor='center', width=130)
        self.cli_list.column('#2', anchor='center', width=200)
        self.cli_list.column('#3', anchor='center', width=200)
        self.cli_list.column('#4', anchor='center', width=100)

        self.cli_list.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        scroll_bar = Scrollbar (self.cli_list)
        scroll_bar.pack(side=RIGHT, fill=Y)

    def save_task(self):
        """ # """
               
        nome = str(self.name_task_entry.get())
        origem = str(self.origin_entry.get())
        destino = str(self.destiny_entry.get())
        intervalo = str(self.interval_entry.get())

        length_caminho =  open(fr"{cwd}/assets/agendamentos.txt", "r", encoding='utf-8')
        length_caminho = length_caminho.readlines()

        if(len(length_caminho) < 3
            and len(nome)       > 1
            and len(origem)     > 1
            and len(destino)    > 1
            and len(intervalo)  > 1):

            caminho =  open(fr"{cwd}/assets/agendamentos.txt", "a", encoding='utf-8')
            caminho.write(f'{nome}_{origem}_{destino}_{intervalo}_ \n')
            caminho.close()
        

        self.name_task_entry.delete(0, END)
        self.origin_entry.delete(0, END)
        self.destiny_entry.delete(0, END)
        self.interval_entry.delete(0, END)


        self.show_tasks()

    def show_tasks(self):
        """ # """
        self.cli_list.delete(*self.cli_list.get_children())
        caminho =  open(fr"{cwd}/assets/agendamentos.txt", "r", encoding='utf-8')
        caminho = caminho.readlines()
        for i in caminho:
            valores = i.split('_')
            self.cli_list.insert("", END, values=(valores[0], valores[1], valores[2], valores[3]))

    def delete_task(self):
        """ # """
        line_delete = self.name_task_delete_entry.get()

        if(len(line_delete) > 2):
            current_file = open(fr"{cwd}/assets/agendamentos.txt", "r", encoding='utf-8')
            current_file = current_file.readlines()

            preserved_lines = []

            for line in current_file:
                if(line.split('_')[0] != line_delete):
                    preserved_lines.append(line)
            
            if(len(preserved_lines) != 3):
                new_file = open(fr"{cwd}/assets/agendamentos.txt", "w", encoding='utf-8')

                if(len(preserved_lines) == 2):
                    new_file.write(preserved_lines[0])
                    new_file.write(preserved_lines[1])
                    new_file.close()
                    self.show_tasks()

                if(len(preserved_lines) == 1):
                    new_file.write(preserved_lines[0])
                    new_file.close()
                    self.show_tasks()

                if(len(preserved_lines) == 0):
                    new_file.close()
                    self.show_tasks()
                
    def start_program(self):
        try:
            os.system('TASKKILL /F /IM script.exe')
        except:
            pass
        os.popen(fr"{cwd}/assets/script.exe")
    

    def Stop_program(self):
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
