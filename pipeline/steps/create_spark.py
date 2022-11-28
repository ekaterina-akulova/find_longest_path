from pyspark.sql import *

spark = SparkSession.builder \
        .master("local[*]") \
        .config("spark.executor.memory", "70g") \
        .config("spark.driver.memory", "50g") \
        .config("spark.memory.offHeap.enabled", "true") \
        .config("spark.memory.offHeap.size", "16g") \
        .config("spark.jars.packages", "graphframes:graphframes:0.8.2-spark3.2-s_2.12") \
        .getOrCreate()
