#coding:utf-8

#这个程序是根据输入的ip或子网返回网络、掩码、广播、反向解析、子网数、IP类型等信息
print "程序说明：这个程序是根据输入的ip或子网返回网络、掩码、广播、反向解析、子网数、IP类型等信息。"

from IPy import IP

ip_input = raw_input('请输入一个IP或使用数字确认掩码的网段地址，如192.168.1.1或192.168.1.0/24: ')
ips = IP(ip_input)

if len(ips) > 1:
    #len(ips) > 1，说明输入的是一个网络地址
    print "你输入的",ips,"是一个网络地址，其中："
    print ips,"的网络地址为",ips.net()
    print ips,"的子网掩码为",ips.netmask()
    print ips,"的广播地址为",ips.broadcast()
    print ips,"的地址反向解析为",ips.reverseNames()[0]
    print ips,"的ip数量有",len(ips),"个"
else:
    #len(ips) < 1，说明输入的是一个ip地址
    print "你输入的",ips,"是一个ip地址，其中："
    print ips,"的十六进制转换地址为",ips.strHex()
    print ips,"的二进制转换地址为", ips.strBin()
    print ips,"的地址类型为", ips.iptype(),"地址"