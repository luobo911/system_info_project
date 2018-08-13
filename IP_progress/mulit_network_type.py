#coding:utf-8

from IPy import IP

#判断ip包含在网段内，采用ip in IP(network)方法
print
print "判断ip包含在网段内，采用ip in IP(network)方法"
print
ip_add1='192.168.100.2'
network1='192.168.100.0/24'
print "本次要判断的ip地址是",ip_add1,"网段是",network1

t_f=ip_add1 in IP(network1)
if t_f == True:
    print "本次ip和网段对比结果是", t_f
    print "因此",ip_add1,"是包含在",network1,"网络中的ip地址"
else:
    print "本次ip和网段对比结果是", t_f
    print "因此",ip_add1,"不是包含在",network1,"网络中的ip地址"

#判断ip包含在网段内，采用ip in IP(network)方法
print
print "判断2个网段是否重叠，采用IPy的overlaps方法"
print
network3='172.16.0.0/23'
network4='172.16.1.0/24'
print "本次要判断的两个网络地址是",network3,"和",network4
t_f2=IP(network3).overlaps(network4)
if t_f2 != 0:
    t_f2_2 ="True"
else:
    t_f2_2 ="False"
if t_f2 != 0:
    print "本次ip和网段对比结果是", t_f2_2
    print network3,"与",network4,"存在重叠"
else:
    print "本次ip和网段对比结果是", t_f2_2
    print network3,"与",network4,"不存在重叠"