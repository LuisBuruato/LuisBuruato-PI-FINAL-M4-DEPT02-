from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("transform").getOrCreate()

df = spark.read.csv("data/raw/data.csv", header=True)

df = df.withColumnRenamed("value","amount")

df.write.mode("overwrite").csv("data/silver/data")

print("Transformación completada (Silver)")