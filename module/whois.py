"""
Coder: indryanto
"""


from assets.warna import *
from bs4 import BeautifulSoup
from assets.fungsi import _headers, write, Request, hapusHTTP, tambahHTTP
import re, os, requests, json

def whoIS(website):
    website = 'http://api.whoapi.com/?apikey=66ca3039356c0287ff63ed472f528478&r=whois&domain={url}&ip='.format(url=website)
    req = Request(website, _timeout=8, _encode=True)
    js = json.loads(req)
    whois = js['whois_raw']
    for result in whois.split('\n'):
        if len(result) != 0:
            write(var='~', color=c, data=result)