#coding:utf-8

import psutil


memery=psutil.virtual_memory()
mem = memery
mem1 = mem.total/1024/1024
mem2 = mem.used/1024/1024
mem3 = mem.free/1024/1024
print "内存使用统计：共计",mem1,"GB，已用",mem2,"GB空闲",mem3,"GB"