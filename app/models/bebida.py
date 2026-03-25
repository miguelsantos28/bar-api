from pydantic import BaseModel

class Bebida(BaseModel):
    nome: str
    preco: float
    estoque: int