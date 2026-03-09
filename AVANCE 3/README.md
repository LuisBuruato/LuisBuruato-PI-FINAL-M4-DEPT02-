# Proyecto Integrador - Avance 3  
## Procesamiento de datos con Apache Spark

### Descripción del proyecto

En esta etapa del proyecto se implementó el procesamiento de datos dentro del Data Lake utilizando Apache Spark y PySpark. El objetivo principal es transformar los datos almacenados en la capa **raw** y generar datasets procesados en la capa **processed**, listos para su análisis.

Como Ingeniero de Datos, el trabajo consiste en desarrollar jobs que permitan combinar, limpiar y transformar los datos para responder preguntas de negocio, aplicando además técnicas de optimización para mejorar el rendimiento del procesamiento.

---

## Tecnologías utilizadas

- Apache Spark
- PySpark
- Python
- Data Lake (estructura raw / processed)

---

## Estructura del proyecto


DE_M4
│
├── spark_jobs
│ └── process_reviews.py
│
└── data
├── raw
│ ├── Patagonia_-41.json
│ └── Riohacha_11_538415.json
│
└── processed
└── weather_analysis.csv


---

## Flujo de procesamiento de datos

1. **Ingesta de datos**

Los datos climáticos en formato JSON se almacenan en la capa **raw** del Data Lake.

2. **Lectura con Spark**

Los archivos JSON se cargan utilizando PySpark:

```python
df_patagonia = spark.read.json(path_patagonia)
df_riohacha = spark.read.json(path_riohacha)

Integración de datasets

Ambos datasets se combinan en un único DataFrame:

df_weather = df_patagonia.unionByName(df_riohacha)

Optimización del procesamiento

Se aplicaron técnicas de optimización:

Repartition para mejorar la distribución del procesamiento.

df_weather = df_weather.repartition(4)

Caching para evitar recalcular operaciones repetidas.

df_weather.cache()

Transformaciones

Se calcularon métricas agregadas por ciudad:

Temperatura promedio

Velocidad promedio del viento

Cantidad total de registros

df_analysis = df_weather.groupBy("city_name").agg(
    avg(col("main.temp")).alias("avg_temperature"),
    avg(col("wind.speed")).alias("avg_wind_speed"),
    count("*").alias("records")
)

Salida de datos

Los resultados se guardan en la capa processed del Data Lake.

Ejecución del job

El procesamiento se ejecuta mediante spark-submit, lo que permite correr el script como un job de Apache Spark.

spark-submit spark_jobs/process_reviews.py
Resultados obtenidos
Ciudad	Temperatura promedio	Velocidad viento promedio	Registros
Patagonia	8.96 °C	3.94 m/s	8784
Riohacha	28.08 °C	4.25 m/s	8784

Estos resultados permiten comparar las condiciones climáticas entre ambas ciudades y responder preguntas de negocio relacionadas con el comportamiento del clima en cada región.

Conclusión

En este avance se implementó un pipeline de procesamiento utilizando Apache Spark que permite transformar datos desde la capa raw hasta processed dentro del Data Lake.

Se aplicaron técnicas de optimización como repartition y cache, además de ejecutar el procesamiento mediante spark-submit, cumpliendo con los requerimientos del proyecto.







