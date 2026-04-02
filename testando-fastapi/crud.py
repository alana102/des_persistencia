from models.veiculo import Veiculo
import pandas as pd 
from deltalake import DeltaTable, write_deltalake, WriterProperties
from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Query
import logging

app = FastAPI()

path = "database/aluguel-carros"
wp = WriterProperties(compression="ZSTD")

@app.get("/veiculos/", response_model=list[Veiculo])
def listar_veiculos(page: int = Query(1, description="Página que deseja visualizar"), 
                    page_size: int = Query(10, description="Qntd de itens por página")):
    dt = DeltaTable(path)
    table = dt.to_pyarrow_table()
    lista = table.to_pylist()

    start = (page - 1) * page_size
    end = start + page_size

    return lista[start:end]


