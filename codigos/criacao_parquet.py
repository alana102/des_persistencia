import pandas as pd

df = pd.DataFrame({
    "nome": ["Alana", "Ivan"],
    "idade": ["19", "21"],
    "cidade": ["Canindé", "Canindé"]
})

df.to_parquet("arquivos/dados.parquet", engine="pyarrow", compression="zstd", index=False)

df_lido = pd.read_parquet("arquivos/dados.parquet", engine="pyarrow")

print(df_lido)



