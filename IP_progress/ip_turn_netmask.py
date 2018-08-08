#coding:utf-8

from IPy import IP

ip_add1 = '172.16.0.0'
netmask1 = '255.255.0.0'

#显示ip_add1网段和netmask1掩码的IP网络地址方法1
print "IP地址:",ip_add1,"和子网掩码:",netmask1,"的组合为:",(IP(ip_add1).make_net(netmask1))

#显示ip_add1网段和netmask1掩码的IP网络地址方法2
#print "IP地址:",ip_add1,"和子网掩码:",netmask1,"的组合为:",(IP(ip_add1/netmask1,make_net=True))