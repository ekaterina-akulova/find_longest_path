from pyspark.sql import *
spark = SparkSession.builder \
        .master("local[*]") \
        .getOrCreate()
