# Documentação da API do Finances Manager

Bem-vindo à documentação da API do projeto `Aplicativo de Gerenciamento Financeiro`! Esta documentação fornece informações detalhadas sobre os endpoints, como usar a API e exemplos de solicitações e respostas.

## Base URL

A base URL da API é `https://finances-manager.onrender.com/`. Todos os endpoints listados abaixo devem ser anexados a essa URL base.

## Endpoints

### Receitas

#### Lista todas as receitas e cria uma nova.
Endpoint: ```localhost:8000/incomes/``` (GET/POST)

#### Retorna, atualiza e deleta uma receita específica.
Endpoint: ```localhost:8000/incomes/{id}/``` (GET/PUT/DELETE)


### Despesas

#### Lista todas as despesas e cria uma nova.
Endpoint: ```localhost:8000/expenses/``` (GET/POST)

#### Retorna, atualiza e deleta uma despesa específica.
Endpoint: ```localhost:8000/expenses/{id}/``` (GET/PUT/DELETE)

### Metas

#### Lista todas as metas e cria uma nova.
Endpoint: ```localhost:8000/goals/``` (GET/POST)

#### Retorna, atualiza e deleta uma meta específica.
Endpoint: ```localhost:8000/goals/{id}/``` (GET/PUT/DELETE)

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
```POST goals/```

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

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.


