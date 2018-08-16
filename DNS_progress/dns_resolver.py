#coding:utf-8

#这个程序是查询输入的域名信息

#以下这段程序用来查询域名的A记录

import dns.resolver

inputdomain=raw_input("查询域名A记录，请输入你要查询的域名：如126.com")
domain_a=dns.resolver.query(inputdomain, 'A')
print '你要查询的',inputdomain,'对应的A记录地址如下'
for i in domain_a.response.answer:
    for j in i.items:
        print j.address

#以下这段程序用来查询域名的MX记录

import dns.resolver

#inputdomain=126.com
inputdomain=raw_input("查询域名MX记录，请输入你要查询的域名：如126.com")
domain_mx=dns.resolver.query(inputdomain, 'MX')
print '你要查询的',inputdomain,'对应的邮箱MX值和mail交换服务器地址如下'
for i in domain_mx:
    print inputdomain,'的MX值是',i.preference,'mail交换服务器地址是',i.exchange

#以下这段程序用来查询域名的NS记录

import dns.resolver

inputdomain=raw_input("查询域名NS记录，请输入你要查询的域名：如126.com")
domain_ns=dns.resolver.query(inputdomain, 'NS')
print '你要查询的',inputdomain,'对应的NS记录地址如下'
for i in domain_ns.response.answer:
    for j in i.items:
        print inputdomain,'的NS记录是',j.to_text()

#以下这段程序用来查询域名的CNAME记录

import dns.resolver

inputdomain=raw_input("查询域名CNAME记录，请输入你要查询的域名：如www.baidu.com")
domain_cname=dns.resolver.query(inputdomain, 'CNAME')
print '你要查询的',inputdomain,'对应的CNAME记录如下'
for i in domain_cname.response.answer:
    for j in i.items:
        print inputdomain,'的CNAME记录是',j.to_text()

