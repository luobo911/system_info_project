#coding:utf-8

import psutil

net_io=psutil.net_io_counters()
net_int_info=psutil.net_io_counters(pernic=True)

print "网络IO统计：",net_io
print "所有网卡IO统计：",net_int_info