#coding:utf-8

from IPy import IP
ip_add1='10.0.0.1'
print ip_add1,"is IPv",IP(ip_add1).version()
ip_add2 = IP('192.168.0.0/24')
print ip_add2,"have",ip_add2.len(),"ips"
print
print "They are"
for x in ip_add2:
    print(x)
