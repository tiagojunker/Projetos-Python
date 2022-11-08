from tkinter import *
from tkinter import ttk
root = Tk()

class Application():
    """ # """
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()
        
    # Configuração da tela
    def tela(self):
        """ # """
        self.root.title("TSG - Copy")
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
        self.bt_limpar = Button(self.frame_1, text='Salvar',
                             bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.02, rely=0.05, relwidth=0.1, relheight=0.10)


        self.bt_limpar = Button(self.frame_1, text='Editar', 
                            bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.14, rely=0.05, relwidth=0.1, relheight=0.10)


        self.bt_limpar = Button(self.frame_1, text='Deletar', 
                            bg='#107db2', fg='white', font = ('verdana', 10, 'bold'))
        self.bt_limpar.place(relx=0.26, rely=0.05, relwidth=0.1, relheight=0.10)


        self.lb_origem = Label(self.frame_1, text='Nome Agendamento', 
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_origem.place(relx=0.02, rely=0.18)


        self.origem_entry = Entry(self.frame_1, 
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.origem_entry.place(relx=0.02, rely=0.26, relwidth=0.45, relheight=0.08)


        self.lb_destino = Label(self.frame_1, text='Intervalo', 
                            bg='#dfe3ee', fg='#1e3743', font = ('verdana', 11, 'bold'))
        self.lb_destino.place(relx=0.52, rely=0.18)


        self.destino_entry = Entry(self.frame_1, 
                            bg='#cfcfcf', fg='#1e3743' ,font=('verdana', 12))
        self.destino_entry.place(relx=0.52, rely=0.26, relwidth=0.15, relheight=0.08)


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

    def lista_frame2(self):
        """ # """
        self.lista_cli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.lista_cli.heading("#0", text='')
        self.lista_cli.heading("#1", text='Nome Agendamento')
        self.lista_cli.heading("#2", text='Origem')
        self.lista_cli.heading("#3", text='Destino')
        self.lista_cli.heading("#4", text='Intervalo')

        self.lista_cli.column('#0', width=1)
        self.lista_cli.column('#1', width=130)
        self.lista_cli.column('#2', width=200)
        self.lista_cli.column('#3', width=200)
        self.lista_cli.column('#4', width=100)

        self.lista_cli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroll_lista = Scrollbar(self.frame_2, orient='vertical')
        self.scroll_lista.place(relx=50, rely=0.1, relwidth=0.1, relheight=0.85)
        self.lista_cli.configure(yscroll = self.scroll_lista.set)


Application()