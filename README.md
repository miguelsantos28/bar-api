#  Bar API

Projeto criado para simular o backend de um bar/estabelecimento que precisa gerenciar pedidos em tempo real: toda venda precisa validar se a bebida existe, se tem estoque suficiente, e atualizar o estoque automaticamente após a venda — sem isso, ficaria fácil vender algo que já acabou. A API cobre cadastro de clientes e bebidas, criação de pedidos com cálculo automático de valor total, e documentação interativa via Swagger para testar cada rota sem precisar de frontend.

API backend desenvolvida com FastAPI para gerenciamento de clientes, bebidas e pedidos.

## Exemplo de uso

**Criando um pedido** — o valor total é calculado automaticamente:

![Pedido criado](https://github.com/user-attachments/assets/0960ba4b-e820-4a77-9e41-85782228512b)

**Estoque antes do pedido (Refrigerante lata em 498):**

<img width="1142" height="772" alt="image" src="https://github.com/user-attachments/assets/62892e69-d3a0-402b-9b86-62977b44d60a" />

**Estoque depois do pedido (Refrigerante lata em 497):**

<img width="1142" height="772" alt="image" src="https://github.com/user-attachments/assets/0c4f0555-1589-471c-88e7-0bf874bc8b4e" />

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
