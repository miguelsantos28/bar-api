import uuid
from database.db import conexao
from database.db import cursor

def criar_bebida(bebida):
    bebida_id = str(uuid.uuid4())
    cursor.execute ("INSERT INTO bebidas (id, nome, preco, estoque) VALUES (?, ?, ?, ?)", (bebida_id, bebida.nome, bebida.preco, bebida.estoque))
    conexao.commit()
    return{
        "id": bebida_id,
        "nome": bebida.nome,
        "preco": bebida.preco,
        "estoque": bebida.estoque
    }
def mostrar_id_bebida(bebida_id):
    cursor.execute ("SELECT * FROM bebidas WHERE id = ?", (bebida_id,))
    bebida_encontrada = cursor.fetchone()
    if bebida_encontrada:
        return {
            "id": bebida_encontrada [0],
            "nome": bebida_encontrada [1],
            "preco": bebida_encontrada [2],
            "estoque": bebida_encontrada [3]
        }
    return None
def mostrar_lista_bebidas():
    cursor.execute("SELECT * FROM bebidas")
    linhas = cursor.fetchall()

    bebidas_formatadas = []

    for linha in linhas:
        bebidas_formatadas.append({"id": linha[0], "nome": linha[1], "preco": linha[2], "estoque": linha[3]})
    return bebidas_formatadas
def atualizar_bebidas(bebida_id, bebida):
    cursor.execute ("SELECT * FROM bebidas WHERE id = ?", (bebida_id,))
    bebida_encontrada = cursor.fetchone()
    if bebida_encontrada:
        cursor.execute("UPDATE bebidas SET nome = ?, preco = ?, estoque = ? WHERE id = ?", (bebida.nome, bebida.preco, bebida.estoque, bebida_id))
        conexao.commit()
        return{
            "id": bebida_id,
            "nome": bebida.nome,
            "preco": bebida.preco,
            "estoque": bebida.estoque
        }
    return None
def apagar_bebida(bebida_id):
    cursor.execute ("SELECT * FROM bebidas WHERE id = ?", (bebida_id,))
    bebida_encontrada = cursor.fetchone()
    if bebida_encontrada:
        cursor.execute("DELETE FROM bebidas WHERE id = ?", (bebida_id,))
        conexao.commit()
        return{
            "id": bebida_encontrada [0],
            "nome": bebida_encontrada [1],
            "preco": bebida_encontrada [2],
            "estoque": bebida_encontrada [3]
        }
    return None
