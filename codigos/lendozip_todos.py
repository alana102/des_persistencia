import zipfile

caminho = 'arquivos/testezip.zip'

with zipfile.ZipFile(caminho, 'r') as zip_ref:
    for arquivo in zip_ref.namelist():
        if arquivo.endswith('.txt'):
            with zip_ref.open(arquivo) as f:
                conteudo = f.read().decode('utf=8')
                print(f"Conteúdo de {arquivo}:")
                print(conteudo)
                print('-' * 60)