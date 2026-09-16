from pathlib import Path
import sqlite3


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", ("Teste 3", "teste.3@example.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?);", (2, "Teste 4", "teste.4@example.com"))
    conexao.commit()
except Exception as e:
    print("Ocorreu um erro:", e)
    conexao.rollback()
