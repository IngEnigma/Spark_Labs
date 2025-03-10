from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

df = spark.sql("SELECT 'Hello World' as hello")

df.show()
df.write.mode("overwrite").json("results")
