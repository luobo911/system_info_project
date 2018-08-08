#coding:utf-8

from IPy import IP

#反向解析地址格式
ip_add1 = IP('192.168.1.20')
print ip_add1,"的反向解析地址格式为",ip_add1.reverseNames()

#检查网络类型是私有地址(PRIVATE)或公有地址(PUBLIC)
print ip_add1,"的网络类型为",ip_add1.iptype(),"地址"

