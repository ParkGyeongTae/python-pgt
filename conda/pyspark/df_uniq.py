from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col

spark = SparkSession \
        .builder \
        .master('local') \
        .appName('my_pyspark_app') \
        .getOrCreate()

data = [
    ('kim', 100),
    ('kim', 90),
    ('lee', 80),
    ('lee', 70),
    ('park', 60)
    ]

schema = StructType([ \
    StructField('name', StringType(), True), \
    StructField('score', IntegerType(), True), \
    ])

df = spark.createDataFrame(data = data, schema = schema)

df.show()

df.select('name').distinct().show()

# dataframe.select('student Name').rdd.flatMap(lambda x: x).collect())
# import pandas as pd

# df.select('name').distinct().collect().toPandas().name.to_list()


# df.printSchema()
# df.show()