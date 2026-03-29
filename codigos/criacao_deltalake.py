import pandas as pd 
from deltalake import write_deltalake, WriterProperties

path = "arquivos/my-delta-rs"

wp = WriterProperties(compression="zstd")

df = pd.DataFrame({"id" : [] ,"nome": [] ,"idade": []})

write_deltalake(path, df, mode="overwrite", writer_properties=wp)