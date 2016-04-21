from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("word counting")
sc = SparkContext(conf=conf)

text_file = sc.textFile("hdfs:///user/README.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b) \
             .sortByKey()
counts.saveAsTextFile("hdfs:///user/out")
