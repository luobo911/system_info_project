#coding:utf-8
import datetime
import psutil

user_info=psutil.users()
boottime=psutil.boot_time()
start_time=datetime.datetime.fromtimestamp(boottime).strftime("%Y-%m-%d %H:%M:%S")

print "现在登录的用户为：",user_info
print "本次系统启动时间为：",start_time