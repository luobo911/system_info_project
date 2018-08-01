#coding:utf-8
#mac os infomation

import psutil
print psutil.pids()
p = psutil.Process(2690)
print 'name is',p.name()
print 'path',p.exe()
print 'status',p.status()
print 'create_time',p.create_time()
print 'uid',p.uids()

print 'gid',p.gids()
#print 'cpu times',p.cpu_times()
#print 'cpu affinity',p.cpu_affinity()
#print 'memonry percent',p.memory_percent()
#print 'menory info',p.memory_info()
#print 'io info',p.io_counters()
#print 'connections info',p.connections()
#print 'num threads',p.num_threads()