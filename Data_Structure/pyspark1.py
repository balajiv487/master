from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField,IntegerType

spark=SparkSession.builder.appName("Python Spark SQL basic example").master("local[*]").getOrCreate()

schema=StructType([
    StructField("id",IntegerType(),True)
])

data = [(1,),(1,) ]# Correct format for matching schema

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()
