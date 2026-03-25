from fastapi import APIRouter
import app.services.bebidas_service as service
from app.models.bebida import Bebida
from fastapi import HTTPException, status

router_bebidas = APIRouter()

@router_bebidas.post('/bebidas', status_code = status.HTTP_201_CREATED)
def criar_bebida_service(bebida: Bebida):
    return service.criar_bebida(bebida)

@router_bebidas.get('/bebidas')
def mostrar_lista_bebidas_service():
    return service.mostrar_lista_bebidas()

@router_bebidas.get('/bebidas/{bebida_id}', status_code = status.HTTP_200_OK)
def mostrar_id_bebida_service(bebida_id: str):
    bebida_encontrada = service.mostrar_id_bebida(bebida_id)
    if not bebida_encontrada:
        raise HTTPException(
           status_code = status.HTTP_404_NOT_FOUND,
            detail = "Bebida não encontrada"
        )
    return bebida_encontrada
@router_bebidas.put('/bebidas/{bebida_id}', status_code = status.HTTP_200_OK)
def atualizar_bebida_service(bebida_id: str, bebida: Bebida):
    bebida_atualizada = service.atualizar_bebidas(bebida_id, bebida)
    if not bebida_atualizada:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Bebida não encontrada"
        )
    return bebida_atualizada
@router_bebidas.delete('/bebidas/{bebida_id}', status_code = status.HTTP_200_OK)
def apagar_bebida_service(bebida_id: str):
    bebida_apagada = service.apagar_bebida(bebida_id)
    if not bebida_apagada:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Bebida não encontrada"
        )
    return bebida_apagada