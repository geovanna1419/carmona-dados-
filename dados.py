import tkinter
from tkinter import *
from usuario import Usuarios

class login:
     def __init__(self, master=None):
         self.janela = Frame(master)
         self.fontePadrao = ("Arial","12")
         self.janela.pack()
         self.titulo = Label(self.janela,text= "informe os dados")
         self.titulo["font"] = ("Arial","29","bold")
         self.titulo.pack()

         self.janela2 = Frame(master)
         self.janela2["padx"] = 20
         self.janela2.pack()

         self.janela3 = Frame(master)
         self.janela3["padx"] = 20
         self.janela3.pack()

         self.janela4 = Frame(master)
         self.janela4["padx"] = 20
         self.janela4.pack()

         self.janela5 = Frame(master)
         self.janela5["padx"] = 20
         self.janela5.pack()

         self.janela6 = Frame(master)
         self.janela6["padx"] = 20
         self.janela6.pack()

         self.janela7 = Frame(master)
         self.janela7["padx"] = 20
         self.janela7.pack()

         self.janela8 = Frame(master)
         self.janela8["padx"] = 20
         self.janela8.pack()

         self.nomeLabel = Label(self.janela2,text="idusuario",font=self.fontePadrao)
         self.nomeLabel.pack(side=LEFT)
         self.nome = Entry(self.janela2)
         self.nome["width"] = 30
         self.nome["font"] = self.fontePadrao
         self.nome.pack(side=LEFT)

         self.btnBuscar = Button(self.janela2)
         self.btnBuscar["text"] = "buscar"
         self.btnBuscar["font"] = ("Calibri", "8")
         self.btnBuscar["width"] = 30
         self.btnBuscar["command"] = self.buscarUsuario
         self.btnBuscar.pack()
         self.btnBuscar["command"] = self.buscarUsuario

         self.senhaLabel = Label(self.janela3, text="nome", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela3)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.numeroLabel = Label(self.janela4, text="telefone", font=self.fontePadrao)
         self.numeroLabel.pack(side=LEFT)
         self.numero = Entry(self.janela4)
         self.numero["width"] = 30
         self.numero["font"] = self.fontePadrao
         self.numero["show"] = "*"
         self.numero.pack(side=LEFT)

         self.emailLabel = Label(self.janela5, text="E-MAIL", font=self.fontePadrao)
         self.emailLabel.pack(side=LEFT)
         self.email = Entry(self.janela5)
         self.email["width"] = 30
         self.email["font"] = self.fontePadrao
         self.email["show"] = "*"
         self.email.pack(side=LEFT)

         self.nomeLabel = Label(self.janela6, text="usúario", font=self.fontePadrao)
         self.nomeLabel.pack(side=LEFT)
         self.nome = Entry(self.janela6)
         self.nome["width"] = 30
         self.nome["font"] = self.fontePadrao
         self.nome["show"] = "*"
         self.nome.pack(side=LEFT)

         self.senhaLabel = Label(self.janela7, text="senha", font=self.fontePadrao)
         self.senhaLabel.pack(side=LEFT)
         self.senha = Entry(self.janela7)
         self.senha["width"] = 30
         self.senha["font"] = self.fontePadrao
         self.senha["show"] = "*"
         self.senha.pack(side=LEFT)

         self.bntInsert = Button(self.janela8)
         self.bntInsert["text"] = "inserir"
         self.bntInsert["font"] = ("Calibri", "8")
         self.bntInsert["width"] = 20
         self.bntInsert["command"] = self.inserirUsuario
         self.bntInsert.pack()
         self.bntInsert["command"] = self.inserirUsuario

         self.bntAlterar = Button(self.janela8)
         self.bntAlterar["text"] = "alterar"
         self.bntAlterar["font"] = ("Calibri", "8")
         self.bntAlterar["width"] = 20
         self.bntAlterar["command"] = self.alterarUsuario
         self.bntAlterar.pack()
         self.bntAlterar["command"] = self.alterarUsuario

         self.bntExcluir = Button(self.janela8)
         self.bntExcluir["text"] = "excluir"
         self.bntExcluir["font"] = ("Calibri", "8")
         self.bntExcluir["width"] = 20
         self.bntExcluir["command"] = self.excluirUsuario
         self.bntExcluir.pack()
         self.bntExcluir["command"] = self.excluirUsuario




    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.selectUser(idusuario)
        self.nomeidusuario.delete(0, END)
        self.nomedusuario.insert(INSERT, user.idusuario)
        self.senhanome.delete(0, END)
        self.senhanome.insert(INSERT, user.nome)
        self.numerotelefone.delete(0, END)
        self.numerotelefone.insert(INSERT, user.telefone)
        self.emailemail.delete(0, END)
        self.emailemail.insert(INSERT, user.email)
        self.nomeusuario.delete(0, END)
        self.nomeusuario.insert(INSERT, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)


    def inserirUsuarios(self):
        user = Usuarios()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.insertUser()
        self.nomeidusuario.delete(0, END)
        self.senhanome.delete(0, END)
        self.numerotelefone.delete(0, END)
        self.emailemail.delete(0, END)
        self.nomeusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def alterarUsuarios(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.updateUser()
        self.nomeidusuario.delete(0, END)
        self.senhanome.delete(0, END)
        self.numerotelefone.delete(0, END)
        self.emailemail.delete(0, END)
        self.nomeusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def excluirUsuarios(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.nomeidusuario.delete(0, END)
        self.senhanome.delete(0, END)
        self.numerotelefone.delete(0, END)
        self.emailemail.delete(0, END)
        self.nomeusuario.delete(0, END)
        self.txtsenha.delete(0, END)

root = Tk()
login(root)
root.mainloop()