with open("arquivos/pessoas.txt", "r") as f:
    doc = f.read()
print(doc.rstrip())