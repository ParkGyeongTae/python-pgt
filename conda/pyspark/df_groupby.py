from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession \
        .builder \
        .master('local') \
        .appName('my_pyspark_app') \
        .getOrCreate()

data = [
    ('kim', 'a', 100),
    ('kim', 'a', 90),
    ('lee', 'a', 80),
    ('lee', 'b', 70),
    ('park', 'b', 60)
    ]

schema = StructType([ \
    StructField('name', StringType(), True), \
    StructField('class', StringType(), True), \
    StructField('score', IntegerType(), True)
    ])
 
df = spark.createDataFrame(data = data, schema = schema)

df.printSchema()
df.show()

df_groupby = df.groupBy().sum()
df_groupby.show()
