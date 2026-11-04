# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Os alunos aprenderão a construir uma API REST completa usando o framework FastAPI, criando endpoints para listar, buscar, criar e remover recursos de uma biblioteca de livros.

## 📝 Tarefas

### 🛠️ Criar o Endpoint de Listagem

#### Descrição
Usando o starter code fornecido, implemente o endpoint `GET /books` que retorna a lista completa de livros da biblioteca.

#### Requisitos
O programa concluído deve:

- Responder a requisições `GET /books` com status 200
- Retornar todos os livros da lista `books` em formato JSON
- Ser executável com `uvicorn main:app --reload` e testável em `http://localhost:8000/docs`

Exemplo de resposta:

```json
[
  {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943}
]
```

### 🛠️ Buscar um Livro por ID

#### Descrição
Implemente o endpoint `GET /books/{book_id}` que retorna um único livro a partir do seu identificador.

#### Requisitos
O programa concluído deve:

- Receber o `book_id` como parâmetro de rota do tipo inteiro
- Retornar o livro correspondente com status 200 quando ele existir
- Retornar status 404 com a mensagem `{"detail": "Book not found"}` quando o livro não existir (use `HTTPException`)

### 🛠️ Cadastrar um Novo Livro

#### Descrição
Implemente o endpoint `POST /books` que recebe os dados de um novo livro no corpo da requisição e o adiciona à biblioteca. Use o modelo Pydantic `Book` fornecido no starter code para validar os dados.

#### Requisitos
O programa concluído deve:

- Validar o corpo da requisição usando o modelo Pydantic `Book`
- Gerar automaticamente um `id` único para o novo livro
- Retornar o livro criado com status 201
- Rejeitar automaticamente requisições com campos faltando ou de tipo incorreto (validação do Pydantic)

Exemplo de requisição:

```json
{"title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}
```

### 🛠️ Remover um Livro

#### Descrição
Complete a API implementando o endpoint `DELETE /books/{book_id}` que remove um livro da biblioteca.

#### Requisitos
O programa concluído deve:

- Remover o livro correspondente ao `book_id` informado
- Retornar status 204 (sem corpo de resposta) quando a remoção for bem-sucedida
- Retornar status 404 com a mensagem `{"detail": "Book not found"}` quando o livro não existir
