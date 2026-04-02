import json
from models import Pessoa

pessoas = [
    Pessoa(id = 1, nome = "Miguel", idade = 1),
    Pessoa(id = 2, nome = "Salah", idade = 7),
    Pessoa(id = 3, nome = "Pérola", idade = 4)
]

with open ("arquivos/pessoas.json", "w") as f:
    json.dump([pessoa.model_dump() for pessoa in pessoas], f, indent = 4)

with open("arquivos/pessoas.json", "r") as f:
    pessoas_desserializadas = [Pessoa.model_validate(pessoa) for pessoa in json.load(f)]

for pessoa in pessoas_desserializadas:
    print(pessoa)