#coding:utf-8

import psutil


cpu_number = psutil.cpu_count()
print "CPU线程数为",cpu_number