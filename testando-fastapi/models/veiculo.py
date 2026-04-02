from pydantic import BaseModel

class Veiculo(BaseModel):
    id : int 
    placa : str
    tipo : str # se é carro ou moto
    modelo : str
    ano : int
    status : str