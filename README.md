# Documentação da API do Finances Manager

Bem-vindo à documentação da API do projeto `Aplicativo de Gerenciamento Financeiro`! Esta documentação fornece informações detalhadas sobre os endpoints, como usar a API e exemplos de solicitações e respostas.

## Base URL

A base URL da API é `https://finances-manager.onrender.com/`. Todos os endpoints listados abaixo devem ser anexados a essa URL base.

## Recursos

A API oferece os seguintes recursos:

### Receitas

- **[GET] /incomes/**: Lista todas as receitas.
- **[POST] /incomes/**: Cria uma nova receita.
- **[GET] /incomes/{id}/**: Retorna detalhes de uma receita específica.
- **[PUT] /incomes/{id}/**: Atualiza uma receita existente.
- **[DELETE] /incomes/{id}/**: Exclui uma receita existente.

### Despesas

- **[GET] /expenses/**: Lista todas as despesas.
- **[POST] /expenses/**: Cria uma nova despesa.
- **[GET] /expenses/{id}/**: Retorna detalhes de uma despesa específica.
- **[PUT] /expenses/{id}/**: Atualiza uma despesa existente.
- **[DELETE] /expenses/{id}/**: Exclui uma despesa existente.

### Metas

- **[GET] /goals/**: Lista todas as metas.
- **[POST] /goals/**: Cria uma nova meta.
- **[GET] /goals/{id}/**: Retorna detalhes de uma meta específica.
- **[PUT] /goals/{id}/**: Atualiza uma meta existente.
- **[DELETE] /goals/{id}/**: Exclui uma meta existente.

## Exemplos

Aqui estão alguns exemplos de solicitações e respostas para os endpoints da API:

### Solicitação GET para listar todas as despesas

```GET /api/expenses/```
Resposta:

```json
[
    {
        "id": 1,
        "description": "Aluguel",
        "amount": 1000.0,
        "date": "2023-08-10"
    },
    {
        "id": 2,
        "description": "Supermercado",
        "amount": 200.0,
        "date": "2023-08-12"
    }
]
```

Solicitação POST para criar uma nova meta
POST /api/goals/


Claro, vou ajudá-lo a criar uma documentação básica para a API do seu projeto finances_manager. Aqui está um exemplo de como você pode estruturar a documentação:

markdown
Copy code
# Documentação da API do finances_manager

Bem-vindo à documentação da API do projeto `finances_manager`! Esta documentação fornece informações detalhadas sobre os endpoints, como usar a API e exemplos de solicitações e respostas.

## Base URL

A base URL da API é `https://finances-manager.onrender.com/api/`. Todos os endpoints listados abaixo devem ser anexados a essa URL base.

## Autenticação

A autenticação não é necessária para acessar a maioria dos endpoints desta API. No entanto, certos endpoints podem exigir autenticação para fins de segurança.

## Recursos

A API oferece os seguintes recursos:

### Receitas

- **[GET] /incomes/**: Lista todas as receitas.
- **[POST] /incomes/**: Cria uma nova receita.
- **[GET] /incomes/{id}/**: Retorna detalhes de uma receita específica.
- **[PUT] /incomes/{id}/**: Atualiza uma receita existente.
- **[DELETE] /incomes/{id}/**: Exclui uma receita existente.

### Despesas

- **[GET] /expenses/**: Lista todas as despesas.
- **[POST] /expenses/**: Cria uma nova despesa.
- **[GET] /expenses/{id}/**: Retorna detalhes de uma despesa específica.
- **[PUT] /expenses/{id}/**: Atualiza uma despesa existente.
- **[DELETE] /expenses/{id}/**: Exclui uma despesa existente.

### Metas

- **[GET] /goals/**: Lista todas as metas.
- **[POST] /goals/**: Cria uma nova meta.
- **[GET] /goals/{id}/**: Retorna detalhes de uma meta específica.
- **[PUT] /goals/{id}/**: Atualiza uma meta existente.
- **[DELETE] /goals/{id}/**: Exclui uma meta existente.

## Exemplos

Aqui estão alguns exemplos de solicitações e respostas para os endpoints da API:

### Solicitação GET para listar todas as despesas

```GET expenses/```

Resposta:

```json
[
    {
        "id": 1,
        "description": "Aluguel",
        "amount": 1000.0,
        "date": "2023-08-10"
    },
    {
        "id": 2,
        "description": "Supermercado",
        "amount": 200.0,
        "date": "2023-08-12"
    }
]
```

### Solicitação POST para criar uma nova meta

```POST /goals/```
Corpo da Solicitação:

```json
{
    "description": "Viagem dos sonhos",
    "target_amount": 5000.0
}
```

Resposta:

```json
{
    "id": 3,
    "description": "Viagem dos sonhos",
    "target_amount": 5000.0,
    "progress": 0.0
}
```
