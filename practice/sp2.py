import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk1.8.0_202"
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\balaj\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = os.environ["PYSPARK_PYTHON"]
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("TestApp") \
    .master("local[*]") \
    .getOrCreate()

df = spark.range(5)
df.show()


import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\balaj\PycharmProjects\pythonProject1\venv\Scripts\python.exe"
