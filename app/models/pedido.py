from pydantic import BaseModel, Field

class Pedido(BaseModel):
    cliente_id: str
    bebida_id: str
    quantidade: int = Field(gt=0)