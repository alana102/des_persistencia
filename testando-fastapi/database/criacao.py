import pandas as pd
from deltalake import WriterProperties, write_deltalake, DeltaTable
import shutil

path = "database/aluguel-carros"
ultimo_id = "database/ultimo_id.seq"

shutil.rmtree(path, ignore_errors=True)

wp = WriterProperties(compression="ZSTD")

df = pd.DataFrame({"id" : pd.Series(dtype="int64"), 
                   "placa" : pd.Series(dtype="string"), 
                   "tipo" : pd.Series(dtype="string"), 
                   "modelo" : pd.Series(dtype="string"), 
                   "ano" : pd.Series(dtype="int64"), 
                   "status" : pd.Series(dtype="string")})

write_deltalake(path, df, mode="overwrite", writer_properties=wp)

with open (ultimo_id, "w") as id:
    id.write("")