import uuid
from database.db import conexao
from database.db import cursor

def criar_cliente(cliente):
    cliente_id = str(uuid.uuid4())
    cursor.execute("INSERT INTO clientes (id, nome, idade) VALUES (?, ?, ?)", (cliente_id, cliente.nome, cliente.idade))
    conexao.commit()
    return {
        "id": cliente_id,
        "nome": cliente.nome,
        "idade": cliente.idade
    }

def mostrar_id_cliente(cliente_id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente_encontrado = cursor.fetchone()
    if cliente_encontrado:
        return {
            "id": cliente_encontrado [0],
            "nome": cliente_encontrado[1],
            "idade": cliente_encontrado[2]
        }
    return None

def apagar_cliente(cliente_id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente_encontrado = cursor.fetchone()

    if cliente_encontrado:
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conexao.commit()
        return{
            "id": cliente_encontrado [0],
            "nome": cliente_encontrado [1],
            "idade": cliente_encontrado [2]
        }
    return None

def mostrar_lista_clientes():
    cursor.execute("SELECT * FROM clientes")
    linhas = cursor.fetchall()

    clientes_formatados = []

    for linha in linhas:
        clientes_formatados.append({"id": linha[0], "nome": linha[1], "idade": linha[2]})
    
    return clientes_formatados

def atualizar_cliente(cliente_id, cliente):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    cliente_encontrado = cursor.fetchone()

    if cliente_encontrado:
        cursor.execute("UPDATE clientes SET nome = ?, idade = ? WHERE id = ?", (cliente.nome, cliente.idade, cliente_id,))
        conexao.commit()
        return{
            "id": cliente_id,
            "nome": cliente.nome,
            "idade": cliente.idade
        }
    
    return None