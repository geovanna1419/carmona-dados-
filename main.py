import tkinter
from tkinter import *

class Login:
   def __init__(self, master=None):
       self.janela = Frame(master)
       self.fontepadrao= ("Arial", "12")
       self.janela.pack()
       self.titulo = Label(self.janela, text="Dados do Usùario")
       self.titulo["font"] = ("arial", "30", "bold")
       self.titulo.pack()

       self.janela2 = Frame(master)
       self.janela2["padx"] = 20
       self.janela2.pack()
       self.nomeLabel = Label(self.janela2, text="nome", font=self.fontepadrao)
       self.nomeLabel.pack(side=LEFT)
       self.nome = Entry(self.janela2)
       self.nome["width"]= 30
       self.nome ["font"]= self.fontepadrao
       self.nome.pack(side=LEFT)

       self.janela2 = Frame(master)
       self.janela2["padx"] = 20
       self.janela2.pack()
       self.nomeLabel = Label(self.janela2, text="Senha ", font=self.fontepadrao)
       self.nomeLabel.pack(side=LEFT)
       self.nome = Entry(self.janela2)
       self.nome["width"]= 30
       self.nome ["font"]= self.fontepadrao
       self.nome.pack(side=LEFT)

       self.janela4 = Frame(master)
       self.janela2["padx"] = 20
       self.janela2.pack()

root = Tk()
Login(root)
root.mainloop()
