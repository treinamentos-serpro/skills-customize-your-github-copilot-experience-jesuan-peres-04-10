"""Building REST APIs with FastAPI - Starter Code

Execute a API com:
    uvicorn main:app --reload

Depois acesse a documentação interativa em:
    http://localhost:8000/docs

Dependências (instale com pip):
    pip install fastapi uvicorn
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Library API")


# Modelo Pydantic usado para validar os dados de um livro
class Book(BaseModel):
    title: str
    author: str
    year: int


# "Banco de dados" em memória com alguns livros iniciais
books: list[dict] = [
    {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
]


# Tarefa 1: implemente o endpoint GET /books
# Dica: use o decorator @app.get("/books")


# Tarefa 2: implemente o endpoint GET /books/{book_id}
# Dica: declare o parâmetro como inteiro: def get_book(book_id: int)
# Use raise HTTPException(status_code=404, detail="Book not found") se não encontrar


# Tarefa 3: implemente o endpoint POST /books
# Dica: use @app.post("/books", status_code=201) e receba um parâmetro do tipo Book


# Tarefa 4: implemente o endpoint DELETE /books/{book_id}
# Dica: use @app.delete("/books/{book_id}", status_code=204)
