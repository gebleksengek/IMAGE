# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


from assets.warna import *
from bs4 import BeautifulSoup
from assets.fungsi import _headers, write, Request, hapusHTTP, tambahHTTP
import re, os, requests, json

def reverseIP(website):
    website = tambahHTTP(website)
    webs = hapusHTTP(website)
    url = 'https://domains.yougetsignal.com/domains.php'
    post = {'remoteAddress' : webs, 'key' : ''}
    request = requests.post(url, headers=_headers, data=post).text.encode('utf-8')
    grab = json.loads(request)
    Status = grab['status']
    IP = grab['remoteIpAddress']
    Domain = grab['remoteAddress']
    Total_Domains = grab['domainCount']
    Array = grab['domainArray']

    if (Status == 'Fail'):
        write(var='#', color=r, data='Gagal melakukan Reverse IP')
    else:
        write(var='$', color=c, data='IP: ' + IP + '')
        write(var='$', color=c, data='Domain: ' + Domain + '')
        write(var='$', color=c, data='Total Domain: ' + Total_Domains + '\n')

        domains = []

        for x, y in Array:
            domains.append(x)

        for res in domains:
            write(var='#', color=b, data=res)