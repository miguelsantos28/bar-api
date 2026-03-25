from fastapi import FastAPI
from app.routes.bebidas import router_bebidas
from app.routes.clientes import router_clientes
from app.routes.pedidos import router_pedidos

app = FastAPI()
app.include_router(router_bebidas)
app.include_router(router_clientes)
app.include_router(router_pedidos)

@app.get("/")
def read_root():
    return {"mensagem": "API do Bar Funcionando"}
