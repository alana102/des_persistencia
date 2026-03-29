import csv

pessoas = [
    {"nome": "Alana", "idade": "19"},
    {"nome": "Ivan", "idade": "21"}
]

with open("arquivos/pessoas.csv", "w", newline="", encoding="utf-8") as file:
    escritor = csv.DictWriter(file, fieldnames=["nome", "idade"])

    escritor.writeheader()

    for p in pessoas:
        escritor.writerow(p)
