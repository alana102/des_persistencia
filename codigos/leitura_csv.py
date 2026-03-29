import csv

with open("arquivos/pessoas.csv", "r", newline="", encoding="utf-8") as file:
    leitor = csv.DictReader(file)

    for linha in leitor:
        print(f"Nome: {linha['nome']}, Idade: {linha['idade']}")