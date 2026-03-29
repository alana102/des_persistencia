from pydantic import BaseModel

class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int