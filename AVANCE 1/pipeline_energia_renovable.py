# ==========================================================
# PIPELINE ETLT - ENERGIA RENOVABLE
# Riohacha (Colombia) vs Patagonia (Argentina)
# Autor: Luis
# ==========================================================

import json
import pandas as pd

# ----------------------------------------------------------
# 1. RUTAS DE ARCHIVOS (RAW)
# ----------------------------------------------------------

archivo_riohacha = r"C:\Users\luisb\Desktop\DE M4\Riohacha_11_538415.json"
archivo_patagonia = r"C:\Users\luisb\Desktop\DE M4\Patagonia_-41.json"


# ----------------------------------------------------------
# 2. FUNCION PARA CARGAR JSON
# ----------------------------------------------------------

def cargar_json(ruta):

    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    return df


# ----------------------------------------------------------
# 3. EXTRACT
# ----------------------------------------------------------

print("Extrayendo datos...")

df_riohacha = cargar_json(archivo_riohacha)
df_patagonia = cargar_json(archivo_patagonia)

df_riohacha["ubicacion"] = "Riohacha"
df_patagonia["ubicacion"] = "Patagonia"


# ----------------------------------------------------------
# 4. LOAD (UNIFICAR DATASETS)
# ----------------------------------------------------------

df = pd.concat([df_riohacha, df_patagonia], ignore_index=True)

print("Datos combinados:", df.shape)

print("\nColumnas del dataset:")
print(df.columns)


# ----------------------------------------------------------
# 5. TRANSFORM
# ----------------------------------------------------------

print("\nTransformando datos...")

# convertir timestamp unix a fecha
df["fecha_hora"] = pd.to_datetime(df["dt"], unit="s")

# variables de tiempo
df["hora"] = df["fecha_hora"].dt.hour
df["fecha"] = df["fecha_hora"].dt.date
df["mes"] = df["fecha_hora"].dt.month

# renombrar columnas para facilitar análisis
df = df.rename(columns={
    "main.temp": "temperatura",
    "main.humidity": "humedad",
    "clouds.all": "nubosidad",
    "wind.speed": "velocidad_viento",
    "rain.1h": "lluvia_1h",
    "snow.1h": "nieve_1h"
})

# reemplazar nulos
df["lluvia_1h"] = df["lluvia_1h"].fillna(0)
df["nieve_1h"] = df["nieve_1h"].fillna(0)


# ----------------------------------------------------------
# 6. CALCULO DE POTENCIAL ENERGETICO
# ----------------------------------------------------------

print("\nCalculando potencial energético...")

# potencial solar estimado
df["potencial_solar"] = (100 - df["nubosidad"]) * (df["temperatura"] / 30)

# potencial eolico estimado
df["potencial_eolico"] = df["velocidad_viento"] ** 3


# ----------------------------------------------------------
# 7. ANALISIS - PREGUNTAS DE NEGOCIO
# ----------------------------------------------------------

print("\n==============================")
print("ANALISIS DE NEGOCIO")
print("==============================")

# ----------------------------------------------------------
# 1 VARIACION SOLAR DURANTE EL DIA
# ----------------------------------------------------------

solar_por_hora = df.groupby(["ubicacion","hora"])["potencial_solar"].mean()

print("\nPromedio potencial solar por hora:")
print(solar_por_hora)


# ----------------------------------------------------------
# 2 PATRONES HISTORICOS DEL VIENTO
# ----------------------------------------------------------

viento_stats = df.groupby("ubicacion")["velocidad_viento"].describe()

print("\nPatrones históricos del viento:")
print(viento_stats)


# ----------------------------------------------------------
# 3 CONDICIONES QUE REDUCEN ENERGIA
# ----------------------------------------------------------

correlacion = df[[
    "nubosidad",
    "lluvia_1h",
    "nieve_1h",
    "potencial_solar"
]].corr()

print("\nRelación clima vs potencial solar:")
print(correlacion)


# ----------------------------------------------------------
# 4 COMPARACION CLIMATICA
# ----------------------------------------------------------

clima_promedio = df.groupby("ubicacion")[[
    "temperatura",
    "velocidad_viento",
    "nubosidad"
]].mean()

print("\nCondiciones climáticas promedio:")
print(clima_promedio)


# ----------------------------------------------------------
# 5 DIAS CON MAYOR Y MENOR POTENCIAL
# ----------------------------------------------------------

energia_dia = df.groupby(["ubicacion","fecha"])[
    ["potencial_solar","potencial_eolico"]
].sum()

max_solar = energia_dia["potencial_solar"].idxmax()
min_solar = energia_dia["potencial_solar"].idxmin()

print("\nDia con MAYOR potencial solar:")
print(max_solar)

print("\nDia con MENOR potencial solar:")
print(min_solar)


# ----------------------------------------------------------
# 8 LOAD → DATASET FINAL
# ----------------------------------------------------------

ruta_salida = r"C:\Users\luisb\Desktop\DE M4\energia_procesada.csv"

df.to_csv(ruta_salida, index=False)

print("\nDataset guardado en:")
print(ruta_salida)

print("\nPipeline completado correctamente")

