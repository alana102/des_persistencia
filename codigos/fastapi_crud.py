import pandas as pd 
from deltalake import DeltaTable, write_deltalake, WriterProperties
from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from models import Pessoa

app = FastAPI()

path = "arquivos/my-delta-rs"
wp = WriterProperties(compression="zstd")

@app.get("/")
def padrao():
    return {"msg" : "Hello World"}

@app.get("/pessoas/", response_model=list[Pessoa])
def listar_pessoas():
    dt = DeltaTable(path)
    lista = dt.to_pyarrow_table().to_pylist()
    return lista


@app.get("/pessoas/{pessoa_id}", response_model=Pessoa)
def ler_pessoa(pessoa_id: int):
    dt = DeltaTable(path)
    pessoa = dt.to_pyarrow_table(filters=[("id", "=", pessoa_id)]).to_pylist()

    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    
    return pessoa[0]

@app.post("/pessoas/", response_model=Pessoa, status_code=HTTPStatus.CREATED)
def adicionar_pessoa(pessoa: Pessoa):
    dt = DeltaTable(path)
    pessoa_ver = dt.to_pyarrow_table(filters=[("id", "=", pessoa.id)]).to_pylist()

    if pessoa_ver:
        raise HTTPException(status_code=400, detail="ID já existe")

    df_new = pd.DataFrame({"id":[pessoa.id], "nome":[pessoa.nome], "idade":[pessoa.idade]})
    write_deltalake(path, df_new, mode="append", writer_properties=wp)
    return pessoa

@app.put("/pessoas/{pessoa_id}", response_model=Pessoa)
def atualizar_pessoa(pessoa_id: int, pessoa_atualizada: Pessoa):
    dt = DeltaTable(path)
    pessoa_ver = dt.to_pyarrow_table(filters=[("id", "=", pessoa_id)]).to_pylist()

    if not pessoa_ver:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
      
    dt.update(
        predicate= f"id = {pessoa_id}",
        updates= {
            "nome": f"'{pessoa_atualizada.nome}'",
            "idade": str(pessoa_atualizada.idade)
        }
    )
    pessoa_atualizada.id = pessoa_id
    return pessoa_atualizada
        

@app.delete("/pessoas/{pessoa_id}")
def remover_pessoa(pessoa_id: int):
    dt = DeltaTable(path)
    pessoa_ver = dt.to_pyarrow_table(filters=[("id", "=", pessoa_id)]).to_pylist()

    if not pessoa_ver:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    
    dt.delete(predicate=f"id = {pessoa_id}")
    return("Pessoa removida com sucesso") 
    









