import zipfile

caminho = 'arquivos/testezip.zip'

nome_arquivo = 'testezip.txt'

with zipfile.ZipFile(caminho, "r") as zip_ref:
    with zip_ref.open(nome_arquivo) as file:
        conteudo = file.read().decode('utf-8')
        print(conteudo)

