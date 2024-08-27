import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuario (
        id usuario integer primary key autoincrement ,
        nome text ,
        telefone text,
        email text,
        usuario text,
        senha text,
        senha text)""")
        self.conexaao.commint()
        c.close()
