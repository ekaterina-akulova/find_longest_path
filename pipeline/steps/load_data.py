from pipeline.steps.create_spark import spark
import pandas as pd

def load_data_pandas(data_path: str):
    df = pd.read_csv(data_path, delimiter=';')
    return df

def load_data(data_path: str):
    df_spark = spark.read.load(data_path,
                     format="csv", sep=";", inferSchema="true", header="true")
    return df_spark