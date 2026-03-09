from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col


def main():

    spark = SparkSession.builder \
        .appName("Weather Data Processing") \
        .getOrCreate()

    path_patagonia = "spark_jobs/data/raw/Patagonia_-41.json"
    path_riohacha = "spark_jobs/data/raw/Riohacha_11_538415.json"

    df_patagonia = spark.read.json(path_patagonia)
    df_riohacha = spark.read.json(path_riohacha)

    df_weather = df_patagonia.unionByName(
        df_riohacha,
        allowMissingColumns=True
    )

    df_weather = df_weather.repartition(4)
    df_weather.cache()

    df_analysis = df_weather.groupBy("city_name").agg(
        avg(col("main.temp")).alias("avg_temperature"),
        avg(col("wind.speed")).alias("avg_wind_speed"),
        count("*").alias("records")
    )

    df_analysis.show()

    # guardar en csv usando pandas
    output_path = "spark_jobs/data/processed/weather_analysis.csv"

    pdf = df_analysis.toPandas()
    pdf.to_csv(output_path, index=False)

    print("Archivo guardado correctamente en processed")

    spark.stop()


if __name__ == "__main__":
    main()