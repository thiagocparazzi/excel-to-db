from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pandas as pd

spark = SparkSession \
    .builder \
    .appName("myApp") \
    .getOrCreate()

data = pd.read_excel(r'D:\Dados\Downloads\teste.xlsx')
data.to_csv('teste.csv', encoding='utf-8', index=False)
data = pd.read_csv("teste.csv")

mySchema = StructType([ StructField("WORKNBR", StringType(), True)\
                       ,StructField("COUNTRY", StringType(), True)\
                       ,StructField("MONEY", FloatType(), True)\
                       ,StructField("ZOO", StringType(), True)])

df = spark.createDataFrame(data,schema=mySchema)
df.show()


