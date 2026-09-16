from pathlib import Path
import sqlite3

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute("CREATE TABLE if NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")


def inserir_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()


def atualizar_cliente(conexao, cursor, email, nome, id):
    data = (email, nome, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    conexao.commit()


def excluir_cliente(conexao, cursor, id):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()


def inserir_clientes_em_lote(conexao, cursor, clientes):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", clientes)
    conexao.commit()


def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes")
    lista=cursor.fetchall()
    for cliente in lista:
        print(dict(cliente))


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = cursor.fetchone()
    print(dict(cliente))


listar_clientes(cursor)
recuperar_cliente(cursor, 3)