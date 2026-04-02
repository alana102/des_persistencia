from faker import Faker
import random
import pandas as pd
from deltalake import WriterProperties, write_deltalake,DeltaTable

path = "database/aluguel-carros"
ultimo_id = "database/ultimo_id.seq"
wp = WriterProperties(compression="ZSTD")

fake = Faker("pt-br")

Faker.seed(0)

tipos = {
    "Carro": [
        "Honda Civic",
        "Toyota Corolla",
        "Chevrolet Onix",
        "Volkswagen Gol"
    ],
    "Moto": [
        "Honda CG 160",
        "Yamaha Fazer 250",
        "Honda Biz",
        "Yamaha MT-03"
    ]
}

status = ["Disponível", "Alugado", "Em manutenção"]

for i in range(10):
    id_atual = 0
    next_id = 0

    with open(ultimo_id, "r") as id:
        id_atual = id.read().strip()

        if id_atual:
            next_id = int(id_atual) + 1

    ano = fake.year()
    placa = fake.license_plate()
    tipo = random.choice(list(tipos.keys()))
    modelo = random.choice(tipos[tipo])
    estado = random.choice(status)

    df_new = pd.DataFrame({"id" : [next_id], "placa": [placa], "tipo" : [tipo], "modelo" : [modelo], "ano" : [ano], "status" : [estado]})
    write_deltalake(path, df_new, mode="append", writer_properties=wp)

    with open(ultimo_id, "w") as id:
        id.write(str(next_id))

dt = DeltaTable(path)
lista = dt.to_pyarrow_table().to_pylist()
print(lista)
    