import sqlite3
conexao = sqlite3.connect('database/banco.db', check_same_thread=False)
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
    id TEXT,
    nome TEXT,
    idade INTEGER
)""")
conexao.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS bebidas (
    id TEXT,
    nome TEXT,
    preco FLOAT,
    estoque INTEGER
)""")
conexao.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos(
    id TEXT,
    cliente_id TEXT,
    bebida_id TEXT,
    quantidade INTEGER,
    valor_total REAL
)""")
conexao.commit()
try:
    cursor.execute("ALTER TABLE pedidos ADD COLUMN valor_total REAL")
    conexao.commit()
except:
    pass