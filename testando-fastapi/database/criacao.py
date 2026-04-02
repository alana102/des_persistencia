import pandas as pd
from deltalake import WriterProperties, write_deltalake

path = "database/aluguel-carros"

wp = WriterProperties(compression="ZSTD")

df = pd.DataFrame({"id" : pd.Series(dtype="int64"), 
                   "placa" : pd.Series(dtype="string"), 
                   "tipo" : pd.Series(dtype="string"), 
                   "modelo" : pd.Series(dtype="string"), 
                   "ano" : pd.Series(dtype="int64"), 
                   "status" : pd.Series(dtype="string")})

write_deltalake(path, df, mode="overwrite", writer_properties=wp)