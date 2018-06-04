#coding:utf-8

import psutil

cpu_cors = psutil.cpu_count()
cpu_nums = psutil.cpu_count(logical=False)
cpu_time_user = psutil.cpu_times().user
print "CPU线程数为：",cpu_cors,"个"
print "CPU物理数为：",cpu_nums,"个"
print "当前用户CPU使用率为：",cpu_time_user