#coding:utf-8

from IPy import IP

ip1='192.168.1.0/24'

#显示strNormal(0),IP网络地址
print ip1,"的网络地址为:",IP(ip1).strNormal(0)

#显示strNormal(1),IP网段及掩码位数
print ip1,"网段和掩码数字形式为:",IP(ip1).strNormal(1)

#显示strNormal(2),IP网段
print ip1,"的网络地址/掩码格式为:",IP(ip1).strNormal(2)

#显示strNormal(3),IP网段
print ip1,"的网络范围为",IP(ip1).strNormal(3)