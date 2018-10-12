# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


from assets.warna import *
from bs4 import BeautifulSoup
from assets.fungsi import _headers, write, Request, hapusHTTP, tambahHTTP
import re, os, requests, json

def crawl(website):
    search = ('site:' + str(hapusHTTP(website)))
    webs = hapusHTTP(website)
    for loop in range(0, 10):
        url = 'https://google.com/search?q=' + str(search) + '&ie=utf-8&oe=utf-8&aq=t&start=' + str(loop) + '0'
        request = requests.get(url, headers=_headers, timeout=5)
        content = request.content
        soup = BeautifulSoup(content, 'lxml')
        sub_links = soup.find_all('h3', class_='r')
        for links in sub_links:
            links = links.a['href']
            if str(webs) in links:
                write(var='~', color=c, data=links)