#coding:utf-8

#这个程序是对域名所有A记录解析的IP列表进行HTTP级别的监控

import dns.resolver,os,httplib

#import os
#import httplib

#定义iplist为域名ip列表变量
iplist=[]
#定义appdomain为需要监控的网址，由键盘输入网址
appdomain=raw_input('请输入你要监控的网址，如www.shenggeol.ml：')

#定义获取iplist，解析域名，解析成功后将IP追加到iplist中
def get_iplist(domain=""):
    try:
        domaina=dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in domaina.response.answer:
        for j in i.items:
            iplist.append(j.address)    #追缴到iplist
    return True

#定义检查ip，定义http连接超时时间(5秒)，定义获取URL的页面前15个字符做可用性校验，定义正常或告警，定义IP解析判断是否存在
def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/",headers={"HOST": appdomain})

        Rpage=conn.getresponse()
        getcontent=Rpage.read(15)

    print getcontent
#    finally:
#        if getcontent==""