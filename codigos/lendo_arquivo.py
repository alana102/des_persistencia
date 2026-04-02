with open("arquivos/pessoas.txt") as f:
    linha = f.readline()
    while linha:
        print(linha.rstrip())
        linha = f.readline()