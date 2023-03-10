from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession \
        .builder \
        .master("local") \
        .appName("my_pyspark_app") \
        .getOrCreate()

data = [
    (0, "kim", 100),
    (1, "kim", 90),
    (2, "lee", 80),
    (3, "lee", 70),
    (4, "park", 60),
    ]

schema = StructType([ \
    StructField('id', IntegerType(), False), \
    StructField('name', StringType(), False), \
    StructField('score', IntegerType(), False), \
])

df = spark.createDataFrame(data=data, schema=schema)
df.printSchema()
df.show()
