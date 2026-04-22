import sqlite3

def conectar():
    return sqlite3.connect("dados.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        valor REAL,
        categoria TEXT,
        data TEXT
    )
    """)

    conexao.commit()
    conexao.close()