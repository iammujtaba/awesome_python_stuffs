import os
import numpy as np
import pandas as pd
from pyarrow import feather
from decorators import timeit

path = os.getcwd()


def generate_random_dataset(limit):
    arr = np.random.randn(limit)
    return pd.DataFrame({f"column_{i}": arr for i in range(10)})


@timeit
def write_into_csv(df):
    df.to_csv("text.csv")


@timeit
def write_into_feather(df):
    with open("text.feather", "wb") as f:
        feather.write_feather(df, f)


df = generate_random_dataset(1000000)
write_into_feather(df)
write_into_csv(df)


"""
Total record - 1000000
Time taken -
'write_into_feather' --> 0.14 sec
'write_into_csv' --> 8.94 sec
"""
