from tkinter import*

class principal:
        def __init__(self):

            janela_principal = Tk()
            janela_principal.geometry("700x575+50+50")
            janela_principal.title("Cadastro de Funcionários")
            #janela_principal.overrideredirect(True)

            txtNDocumento   = StringVar()
            txtAssunto      = StringVar()
            txtDQFR         = StringVar()

            a = Label(janela_principal)
            a.pack(side=TOP)

            b = Label(janela_principal)
            b.pack(side=BOTTOM)

            b1 = Label(janela_principal)
            b1.pack()

            c = Label(janela_principal)
            c.pack(pady=14)

            d = Label(b1, text="Nome:   ", font=("Gentium Basic", 11))
            d.grid(row=0, column=0, sticky=N)
            d1 = Entry(b1, width=20, textvariable=txtNDocumento, font=("Gentium Basic", 11), justify=CENTER)
            d1.grid(row=1, column=0)
            e = Label(b1, text="Idade:   ", font=("Gentium Basic", 11))
            e.grid(row=0, column=1, sticky=N)
            e1 = Entry(b1, width=20, textvariable=txtAssunto, font=("Gentium Basic", 11))
            e1.grid(row=1, column=1)

            f = Label(b1, text="Ocupação:", font=("Gentium Basic", 11))
            f.grid(row=0, column=2, sticky=N)
            f1 = Entry(b1, width=20, textvariable=txtDQFR, font=("Gentium Basic", 11))
            f1.grid(row=1, column=2)

            g = Button(b1, text="ADICIONAR", width=12, height=2, relief=FLAT,  activebackground="#4169E1", activeforeground="WHITE", background="#4169E1", foreground="WHITE")
            g.grid(row=0, column=3, rowspan=2, padx=15)
            rolagem = Scrollbar(c)
            rolagem.grid(row=0, column=1, sticky=N+S)
            caixa_exibição = Listbox(c, relief=SOLID, border=1, width=80, height=25, font=("Gentium Basic", 11))
            caixa_exibição.grid(row=0, column=0)


            #for i in range(100):
            #    caixa_exibição.insert(END, i)

            # attach listbox to scrollbar
            caixa_exibição.config(yscrollcommand=rolagem.set)
            rolagem.config(command=caixa_exibição.yview)

            janela_principal.mainloop()


principal()
