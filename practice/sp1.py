import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StructField, StringType

spark=SparkSession.builder.appName("test").master("local[*]").getOrCreate()
existing_data_list = [(1,"Alice", 34, "Math"), (2,"Bob", 45, "Science"), (3,"Catherine", 29, "History")]
existing_df_columns =StructType([
    StructField("id",IntegerType(),True),
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True),
    StructField("class",StringType(),True)
])
existing_df = spark.createDataFrame(existing_data_list, existing_df_columns)
source_data_list = [(1,"Alice", 34, "Math"), (2,"Bob", 45, "Science"), (3,"Catherine", 29, "History"),(4,"Bonney", 29, "Computer")]

source_df_columns=StructType([
    StructField("id",IntegerType(),True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("class", StringType(), True)
])

source_df=spark.createDataFrame(source_data_list,source_df_columns)
existing_df.show()
source_df.show()

new_records_DF=source_df.alias("sf").join(existing_df.alias("ef") ,"id","LEFTANTI")
new_records_DF.show()
incremental_df=source_df.exceptAll(existing_df)
incremental_df.show()