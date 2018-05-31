import psutil


cpu_number = psutil.cpu_count()
print "CPU cores is", cpu_number