import re

import pandas as pd
from pyspark.sql.functions import mean
from matplotlib import pyplot as plt
import pyspark.sql.functions as F

columns_accordance = {'source_key': 'new_key'}

def preprocessing(df: pd.DataFrame):
    df = df.head(10000)
    df = df[df.cnt > df.cnt.mean()]
    df = df.drop_duplicates()

    df = df.dropna()
    df = df[(df.src != '0.0.0.0') &
            (df.dst != '0.0.0.0') &
            (df.src != '127.0.0.1') &
            (df.src != df.dst)]
    # df.hist(bins=10)
    # plt.show()
    return df

def preprocessing_spark(df, num):
    df = df.na.drop()
    df = df.distinct()
    df = df.filter(df.src != '0.0.0.0')
    df = df.filter(df.dst != '0.0.0.0')
    df = df.filter(df.src != '127.0.0.1')
    df = df.filter(df.dst != '127.0.0.1')
    # not_digit = re.compile('[a-zA-Z]')
    # not_digit.match(dst)
    # df = df[df.dst]
    df = df.filter(df.src != df.dst)
    # print("Before filtering by count df has ", df.count(), " rows.")
    mean_num = df.select(F.mean("cnt")).collect()[0][0]
    df = df.filter(df.cnt > str(mean_num))
    # print("After filtering by count df has ", df.count(), " rows.")
    df = df.take(num)
    print("Taking ", num, "rows.\n\n\n")

    return df
