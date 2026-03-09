from pyspark.sql import SparkSession


def main():

    # Crear sesión de Spark en modo local (importante para Windows)
    spark = SparkSession.builder \
        .appName("TestSpark") \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .getOrCreate()

    print("Spark session creada correctamente")

    # Datos de prueba
    data = [
        ("Luis", 30),
        ("Ana", 25),
        ("Carlos", 40)
    ]

    # Crear DataFrame
    df = spark.createDataFrame(data, ["nombre", "edad"])

    print("Mostrando DataFrame:")

    df.show()

    # Detener Spark
    spark.stop()


if __name__ == "__main__":
    main()