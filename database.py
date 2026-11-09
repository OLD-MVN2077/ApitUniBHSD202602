import sqlite3


def conectar_banco():
	conn = sqlite3.connect("banco_a3.db")
	conn.row_factory = sqlite3.Row
	return conn


def criar_tabelas():
	conn = conectar_banco()
	try:
		conn.execute('''
			CREATE TABLE IF NOT EXISTS registros (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				titulo TEXT NOT NULL,
				descricao TEXT,
				ativo BOOLEAN DEFAULT TRUE
			)
		''')
		conn.commit()
	finally:
		conn.close()
