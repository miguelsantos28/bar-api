from fastapi import APIRouter
import app.services.clientes_service as service
from app.models.cliente import Cliente
from fastapi import HTTPException, status

router_clientes = APIRouter()

@router_clientes.post('/cliente/', status_code = status.HTTP_201_CREATED)
def criar_cliente_service(cliente: Cliente):
    return service.criar_cliente(cliente)

@router_clientes.get('/cliente/{cliente_id}', status_code = status.HTTP_200_OK)
def mostrar_id_cliente_service(cliente_id: str):
    encontrado = service.mostrar_id_cliente(cliente_id)

    if not encontrado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Cliente não encontrado"
        )
    return encontrado

@router_clientes.delete('/cliente/{cliente_id}', status_code = status.HTTP_200_OK)
def apagar_cliente_service(cliente_id: str):
    deletado = service.apagar_cliente(cliente_id)
    
    if not deletado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Cliente não encontrado"
        )
    return deletado

@router_clientes.get('/clientes')
def mostrar_lista_clientes_service():
    return service.mostrar_lista_clientes()

@router_clientes.put('/cliente/{cliente_id}', status_code = status.HTTP_200_OK)
def atualizar_cliente_service(cliente_id: str, cliente: Cliente):
    atualizado = service.atualizar_cliente(cliente_id, cliente)
    if not atualizado:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Cliente não encontrado"
        )
    return atualizado

