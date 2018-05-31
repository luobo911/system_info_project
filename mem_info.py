import psutil


memery=psutil.virtual_memory()
mem = memery
mem1 = mem.total/1024/1024
mem2 = mem.used/1024/1024
mem3 = mem.free/1024/1024
print "memery info:total",mem1,"used",mem2,"free",mem3