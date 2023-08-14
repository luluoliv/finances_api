# Finances Manager API Documentation

Welcome to the API documentation for the `Financial Management Application` project! This documentation provides detailed information about endpoints, how to use the API, and sample requests and responses.

## Base URL

The API base URL is `https://finances-manager.onrender.com/`. All endpoints listed below must be appended to this base URL.

## Endpoints

### Revenues

#### Lists all recipes and creates a new one.
Endpoint: ```localhost:8000/incomes/``` (GET/POST)

#### Returns, updates and deletes a specific recipe.
Endpoint: ```localhost:8000/incomes/{id}/``` (GET/PUT/DELETE)


### Expenses

#### Lists all expenses and creates a new one.
Endpoint: ```localhost:8000/expenses/``` (GET/POST)

#### Returns, updates, and deletes a specific expense.
Endpoint: ```localhost:8000/expenses/{id}/``` (GET/PUT/DELETE)

### Goals

#### Lists all goals and creates a new one.
Endpoint: ```localhost:8000/goals/``` (GET/POST)

#### Returns, updates, and deletes a specific goal.
Endpoint: ```localhost:8000/goals/{id}/``` (GET/PUT/DELETE)

## Examples

Here are some examples of requests and responses for the API endpoints:

### GET request to list all expenses

```GET expenses/```
Response:

```json
[
    {
        "id": 1,
        "description": "Rent",
        "amount": 1000.0,
        "date": "2023-08-10"
    },
    {
        "id": 2,
        "description": "Supermarket",
        "amount": 200.0,
        "date": "2023-08-12"
    }
]
```

### POST request to create a new goal
```POST goals/```

```json
{
    "description": "Dream trip",
    "target_amount": 5000.0
}
```

Response:
```json
{
    "id": 3,
    "description": "Dream trip",
    "target_amount": 5000.0,
    "progress": 0.0
}
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
