import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, when, avg
from functools import reduce

# -----------------------------
# Rutas
# -----------------------------
BASE_DIR = r"C:\Users\luisb\Desktop\DE_M4\AVANCE 3\spark_jobs"

# Archivos JSON raw desde AVANCE 1
RAW_JSON_FILES = [
    r"C:\Users\luisb\Desktop\DE_M4\AVANCE 1\Patagonia_-41.json",
    r"C:\Users\luisb\Desktop\DE_M4\AVANCE 1\Riohacha_11_538415.json"
]

PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
PROCESSED_PARQUET = os.path.join(PROCESSED_DIR, "weather_parquet")
PROCESSED_CSV = os.path.join(PROCESSED_DIR, "weather_clean.csv")

os.makedirs(PROCESSED_DIR, exist_ok=True)
print(f"✅ Carpeta procesada lista: {PROCESSED_DIR}")

# -----------------------------
# Spark Session (Windows-safe)
# -----------------------------
spark = SparkSession.builder \
    .appName("Tercer Avance - Transformaciones Optimización") \
    .config("spark.sql.shuffle.partitions", 4) \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()
print("✅ Spark session creada")

# -----------------------------
# Cargar y combinar JSON dinámicamente
# -----------------------------
dfs = []
for f in RAW_JSON_FILES:
    df = spark.read.json(f)
    print(f"✅ {f} cargado con {df.count()} filas")
    dfs.append(df)

df_json = reduce(lambda a, b: a.unionByName(b, allowMissingColumns=True), dfs)

# -----------------------------
# Transformaciones básicas
# -----------------------------
for col_name in ["temperature", "humidity"]:
    if col_name in df_json.columns:
        df_json = df_json.withColumn(col_name, col(col_name).cast("double"))

if "date" in df_json.columns:
    df_json = df_json.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# -----------------------------
# Transformación de negocio
# -----------------------------
if "temperature" in df_json.columns:
    df_json = df_json.withColumn(
        "temp_category",
        when(col("temperature") < 10, "Frío")
        .when(col("temperature") < 25, "Templado")
        .otherwise("Calor")
    )
else:
    df_json = df_json.withColumn("temp_category", col("city_name"))

# -----------------------------
# Manejo de columnas STRUCT para CSV
# -----------------------------
if 'clouds' in df_json.columns:
    df_json = df_json.withColumn("clouds_all", col("clouds.all"))

if 'rain' in df_json.columns:
    df_json = df_json.withColumn("rain_1h", col("rain.1h"))
    df_json = df_json.withColumn("rain_3h", col("rain.3h"))

if 'snow' in df_json.columns:
    df_json = df_json.withColumn("snow_1h", col("snow.1h"))
    df_json = df_json.withColumn("snow_3h", col("snow.3h"))

# -----------------------------
# Optimización
# -----------------------------
df_json.cache()
df_json = df_json.repartition(4, "temp_category")

# -----------------------------
# Guardar resultados
# -----------------------------
df_json.write.mode("overwrite").partitionBy("temp_category").parquet(PROCESSED_PARQUET)
df_json.coalesce(1).write.mode("overwrite").option("header", True).csv(PROCESSED_CSV)

print(f"Se guardarán los siguientes archivos en {PROCESSED_DIR}:")
print(f"- Parquet particionado por 'temp_category': {PROCESSED_PARQUET}")
print(f"- CSV combinado: {PROCESSED_CSV}")

# -----------------------------
# Promedio de temperatura por categoría
# -----------------------------
if "temperature" in df_json.columns:
    avg_df = df_json.groupBy("temp_category").agg(avg("temperature").alias("avg_temp"))
    avg_df.show()

spark.stop()
print("✅ Spark session cerrada, procesamiento completo")