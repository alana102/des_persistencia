with open("arquivos/aflor-loshermanos.txt", "w", encoding="utf-8") as f:
    while True:
        linha = input()
        if linha == "":
            break
        f.write(f"{linha}\n")