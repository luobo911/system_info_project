#coding:utf-8

import psutil

disk_info=psutil.disk_partitions()
disk_usage=psutil.disk_usage("/")
disk_io=psutil.disk_io_counters()


print "本机磁盘信息：",disk_info
print "磁盘使用状态：",disk_usage
print "当前磁盘IO总数为",disk_io