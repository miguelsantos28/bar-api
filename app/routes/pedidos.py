from fastapi import APIRouter
import app.services.pedidos_service as service
from app.models.pedido import Pedido
from fastapi import HTTPException, status

router_pedidos = APIRouter()

@router_pedidos.post('/pedidos', status_code = status.HTTP_201_CREATED)
def criar_pedido_service(pedido: Pedido):
    try:
        pedido_criado = service.criar_pedido(pedido)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if not pedido_criado:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Cliente ou bebida não encontrado"
        )
    return pedido_criado
    
@router_pedidos.get('/pedidos')
def mostrar_lista_pedidos_service():
    return service.mostrar_lista_pedidos()

@router_pedidos.get('/pedidos/{pedido_id}', status_code = status.HTTP_200_OK)
def mostrar_id_pedido_service(pedido_id: str):
    encontrado = service.mostrar_id_pedido(pedido_id)

    if not encontrado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Pedido não encontrado"
        )
    return encontrado

@router_pedidos.delete('/pedidos/{pedido_id}', status_code = status.HTTP_200_OK)
def apagar_pedido_service(pedido_id: str):
    deletado = service.apagar_pedido(pedido_id)
    
    if not deletado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Pedido não encontrado"
        )
    return deletado

@router_pedidos.put('/pedidos/{pedido_id}', status_code = status.HTTP_200_OK)
def atualizar_pedido_service(pedido_id: str, pedido: Pedido):
    atualizado = service.atualizar_pedido(pedido_id, pedido)
    if not atualizado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Pedido não encontrado ou dados inválidos"
        )
    return atualizado
