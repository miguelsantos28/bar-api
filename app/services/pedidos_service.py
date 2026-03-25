import uuid
from database.db import conexao
from database.db import cursor
from app.services.clientes_service import mostrar_id_cliente
from app.services.bebidas_service import mostrar_id_bebida

def criar_pedido(pedido):
    pedido_id = str(uuid.uuid4())

    cliente = mostrar_id_cliente(pedido.cliente_id)
    if not cliente:
        return None
    bebida = mostrar_id_bebida(pedido.bebida_id)
    if not bebida:
        return None
    
    estoque_atual = bebida["estoque"]
    preco_da_bebida = bebida["preco"]

    if pedido.quantidade > estoque_atual:
        raise ValueError ("Estoque insuficiente")

    novo_estoque = estoque_atual - pedido.quantidade
    valor_total = preco_da_bebida * pedido.quantidade

    cursor.execute("INSERT INTO pedidos (id, cliente_id, bebida_id, quantidade, valor_total) VALUES (?, ?, ?, ?, ?)", (pedido_id, pedido.cliente_id, pedido.bebida_id, pedido.quantidade, valor_total))
    cursor.execute("UPDATE bebidas SET estoque = ? WHERE id = ?", (novo_estoque, pedido.bebida_id))
    conexao.commit()


    return{
        "id": pedido_id,
        "cliente_id": pedido.cliente_id,
        "bebida_id": pedido.bebida_id,
        "quantidade": pedido.quantidade,
        "valor_total": valor_total
    }

def mostrar_lista_pedidos():
    cursor.execute("SELECT * FROM pedidos")
    linhas = cursor.fetchall()

    pedidos_formatados = []

    for linha in linhas:
        pedidos_formatados.append({"id": linha[0], "cliente_id": linha[1], "bebida_id": linha[2], "quantidade": linha[3], "valor_total": linha[4]})
    return pedidos_formatados

def mostrar_id_pedido(pedido_id):
    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
    pedido_encontrado = cursor.fetchone()
    if not pedido_encontrado:
        return None
    
    return{
        "id": pedido_encontrado [0],
        "cliente_id": pedido_encontrado [1],
        "bebida_id": pedido_encontrado [2],
        "quantidade": pedido_encontrado [3],
        "valor_total": pedido_encontrado [4]
    }
def apagar_pedido(pedido_id):
    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id, ))
    pedido_encontrado = cursor.fetchone()
    if not pedido_encontrado:
        return None
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    conexao.commit()

    return{
        "id": pedido_encontrado [0],
        "cliente_id": pedido_encontrado [1],
        "bebida_id": pedido_encontrado [2],
        "quantidade": pedido_encontrado [3],
        "valor_total": pedido_encontrado [4]
    }
    
def atualizar_pedido(pedido_id, pedido):
    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
    pedido_encontrado = cursor.fetchone()
    if not pedido_encontrado:
        return None
    
    cliente = mostrar_id_cliente(pedido.cliente_id)
    if not cliente:
        return None

    bebida = mostrar_id_bebida(pedido.bebida_id)
    if not bebida:
        return None

    preco_da_bebida = bebida["preco"]
    valor_total = preco_da_bebida * pedido.quantidade

    cursor.execute("""UPDATE pedidos SET cliente_id = ?, bebida_id = ?, quantidade = ?, valor_total = ? WHERE id = ?""",
     (pedido.cliente_id, pedido.bebida_id, pedido.quantidade, valor_total, pedido_id))
    conexao.commit()

    return {
    "id": pedido_id,
    "cliente_id": pedido.cliente_id,
    "bebida_id": pedido.bebida_id,
    "quantidade": pedido.quantidade,
    "valor_total": valor_total
}
