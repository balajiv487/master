from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField,DoubleType, IntegerType, StringType

spark=SparkSession.builder.appName("t").master("local[*]").getOrCreate()
schema=StructType([
    StructField("Sales_ID",IntegerType(),True),
    StructField("Product",StringType(),True),
    StructField("Quantity",IntegerType(),True),
    StructField("Price",DoubleType(),True)
    

])
