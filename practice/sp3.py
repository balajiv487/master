import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,upper,when, lit,current_timestamp
spark=SparkSession.builder.appName("").master("local[*]").getOrCreate()

def red_data_from_s3(spark,path,file_format="parquet"):
        df=spark.read.format(file_format).load(path)
        return df

def clean_customer_data(df):
   df1=df.withColumn(col("customer_name"),upper(col("customer_name")))\
       .withColumn(col("is_active"),when(col("status")=="active",lit(1).otherwise(lit(0))))\
       .withColumn(col("ingest_time"),current_timestamp())
   return df1

def join_customer_orders(customer_df,order_df):
    join_df=customer_df.join(order_df,on=customer_df["customer_id"]==order_df["customer_id"],how="inner").drop(col("customer_id"))
    return join_df

def write_to_redshift(df,jdbc_url,table_name,props):
    df.write.jdbc(url=jdbc_url,table=table_name,properties=props)

def run_pipeline():
    customer_df=red_data_from_s3(spark,"s3://a/b/c","csv")
    order_df = red_data_from_s3(spark, "s3://a/b/c", "csv")
    cleaned_customers=clean_customer_data(customer_df)
    final_df=join_customer_orders(cleaned_customers,order_df)
    jdbc_url="jdbc:jdbc:postgresql://localhost:5432/a"
    props={
        "username":"bnaidu",
        "password":"Thehindu@17",
        "port":"5432",
        "driver":"org.postgresql.Driver"
        }
    write_to_redshift(final_df,jdbc_url,table_name="abc.customers",props=props)

    if __name__=="__main__":
        run_pipeline()