from pipeline.steps.create_spark import spark

def load_data(data_path: str):
    df_spark = spark.read.load(data_path,
                     format="csv", sep=";", inferSchema="true", header="true")
    return df_spark