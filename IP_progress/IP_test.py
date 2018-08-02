#coding:utf-8

from IPy import IP

#判断ip_add1的ip地址类型是IPv4 or IPv6
ip_add1='10.0.0.1'
print ip_add1,"是IPv",IP(ip_add1).version()

#判断ip_add2中有多少ip数量，并显示所有ip_add2地址
ip_add2 = IP('192.168.0.0/30')
print ip_add2,"共有",ip_add2.len(),"个ip地址"
print "ip列表如下："
for x in ip_add2:
    print(x)
