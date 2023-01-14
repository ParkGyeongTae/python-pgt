import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import pandas as pd

conf = pyspark.SparkConf().setAppName('appName').setMaster('local')
sc = pyspark.SparkContext(conf = conf)
spark = SparkSession(sc)

df_test = pd.DataFrame({ # 2
    'a': [1, 2, 3],
    'b': [10.0, 3.5, 7.315],
    'c': ['apple', 'banana', 'tomato']
})

df_spark = spark.createDataFrame(df_test) # 3

df_spark.show() # 4
df_spark.show(2) # 5
df_spark.printSchema() # 6
