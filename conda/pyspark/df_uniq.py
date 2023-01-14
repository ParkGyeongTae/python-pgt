from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

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

df_unique_name = df.select('name').distinct()
df_unique_name.show()

# 방법 1과 방법 2 둘다 동일한 결과지만, 방법 2가 더 빠르다

# 방법 1
print(df.select('name').rdd.flatMap(lambda x: x).collect())
print(df.select('name').distinct().rdd.flatMap(lambda x: x).collect())

# 방법 2
print(list(df.select('name').toPandas()['name']))
print(list(df.select('name').toPandas()['name'].unique()))
