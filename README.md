API backend desenvolvida com FastAPI para gerenciamento de:

- Clientes
- Bebidas
- Pedidos

##  Tecnologias
- Python
- FastAPI
- SQLite
- Pydantic

##  Funcionalidades

### Clientes
- Criar cliente
- Listar clientes
- Buscar por ID
- Atualizar
- Deletar

### Bebidas
- CRUD completo

### Pedidos
- Criar pedido
- Validação de cliente e bebida
- Controle de estoque automático
- Cálculo de valor total

##  Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload