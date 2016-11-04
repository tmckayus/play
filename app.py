# spark-basic.py
import sys
import time
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

def mod(x):
    return (x, x % 2)

print "this is me!"
print('\n'.join(sys.path))
rdd = sc.parallelize(range(1000)).map(mod).take(30)
print rdd
print("sleeping for 10 minutes")
time.sleep(600)
