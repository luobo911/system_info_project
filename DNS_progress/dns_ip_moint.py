#coding:utf-8

#这个程序是对域名所有A记录解析的IP列表进行HTTP级别的监控

import dns.resolver
import os
import httplib



#定义iplist为域名ip列表变量
iplist=[]
#定义appdomain为需要监控的网址，由键盘输入网址
appdomain=raw_input('请输入你要监控的网址，如www.shenggeol.ml：')

#定义获取iplist，解析域名，解析成功后将IP追加到iplist中
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')     #解析A记录
    except Exception,e:
        print "DNS解析有误:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)    #追缴到iplist
    return True

#定义检查ip，定义http连接超时时间(5秒)，定义获取URL的页面前15个字符做可用性校验，定义正常或告警，定义IP解析判断是否存在
def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)     #定义http连接超时时间为5秒
    conn=httplib.HTTPConnection(checkurl)     #创建http连接对象

    try:
        conn.request("GET", "/",headers={"HOST": appdomain})    #发起URL请求，添加host主机头

        Rpage=conn.getresponse()
        getcontent=Rpage.read(15)     #获取URL页面前15个字符，以便做可用性校验


    finally:
        if getcontent=="<!doctype html>":     #监控URL页的内容，一般是事先定义好的，比如"HTTP200"等

            print ip+"[ 网站正常 ]"
        else:
            print ip+"[ 网站状态异常 ]"

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
        else:
            print "DNS地址解析错误"