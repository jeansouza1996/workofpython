from tkinter import *

"""
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Usando uma API")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()
        root.title("Cadastro de Funcionários")

root = Tk()
Application(root)
root.mainloop()

"""

#Aprendendo a criar uma interface

root = Tk()

root.geometry("1350x750")
root.title("Sistema")
root.configure(background="gray")

Top = Frame(root, width=1350, height=100, bd=9, relief="flat")
Top.pack(side=TOP)


Left = Frame(root, width=900, height=640, bd=9, relief="flat")
Left.pack(side=LEFT)
Left.configure(background="darkgrey")

Right = Frame(root, width=445, height=640, bd=9, relief="flat")
Right.pack(side=RIGHT)
Right.configure(background="yellow")

lblTitulo = Label(Top, font=("Arial", 20, "bold"), text="CRUD Funcionários")
lblTitulo.grid(row=0, column=0)

root.mainloop()
