#  Bar API

Projeto criado para simular o backend de um bar/estabelecimento que precisa gerenciar pedidos em tempo real: toda venda precisa validar se a bebida existe, se tem estoque suficiente, e atualizar o estoque automaticamente após a venda — sem isso, ficaria fácil vender algo que já acabou. A API cobre cadastro de clientes e bebidas, criação de pedidos com cálculo automático de valor total, e documentação interativa via Swagger para testar cada rota sem precisar de frontend.

API backend desenvolvida com FastAPI para gerenciamento de clientes, bebidas e pedidos.

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
```

##  Documentação
Acesse no navegador:
http://127.0.0.1:8000/docs
