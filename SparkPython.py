import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql import functions
from pyspark import SparkConf
# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=8888, stdoutToServer=True, stderrToServer=True)

class SparkPython:

    def main(self):
        # create spark session
        spark = SparkSession\
            .builder\
            .appName("SparkPython")\
            .getOrCreate()
        # create initial function
        dataframe = spark.read.text("input.txt")
        # count words
        words = dataframe\
            .select(functions.split(functions.col("value"), " ").alias("words"))\
            .select(functions.explode(functions.col("words")).alias("word"))\
            .groupby("word")\
            .count()\
            .orderBy(functions.col("count").desc())
        words.show()
        spark.stop()

if __name__ == '__main__':
    spark = SparkPython()
    spark.main()
