import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk1.8.0_202" # Replace as needed

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestApp") \
    .master("local[*]") \
    .getOrCreate()

print("Spark session created successfully")
spark.stop()
