print("Iniciando ingesta desde Airbyte...")

import pandas as pd

data = {
    "id":[1,2,3],
    "name":["A","B","C"],
    "value":[100,200,300]
}

df = pd.DataFrame(data)

df.to_csv("data/raw/data.csv", index=False)

print("Datos guardados en capa RAW")