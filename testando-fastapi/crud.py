from models.veiculo import Veiculo
import pandas as pd 
from deltalake import DeltaTable, write_deltalake, WriterProperties
from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Query
import logging
import pyarrow.dataset as ds

app = FastAPI()

path = "database/aluguel-carros"
wp = WriterProperties(compression="ZSTD")

# Dúvida: o dataset.to_table() carrega dados na memória, mas eu não como não carregar
@app.get("/veiculos/", response_model=list[Veiculo])
def listar_veiculos(page: int = Query(1, description="Página que deseja visualizar"), 
                    page_size: int = Query(10, description="Qntd de itens por página")):
    dataset = ds.dataset(path, format="parquet")

    start = (page-1) * page_size

    table = dataset.to_table()
    table = table.sort_by([("id", "ascending")])
    table = table.slice(start, page_size)

    return table.to_pylist()


