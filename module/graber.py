# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


from assets.warna import *
from bs4 import BeautifulSoup
from assets.fungsi import _headers, write, Request, hapusHTTP, tambahHTTP
import re, os, requests, json

def graber(website):
    website = tambahHTTP(website)
    request = requests.get(website, timeout=5, headers=_headers).headers.items()
    for headers in request:
        res = headers[0] + ': ' + headers[1]
        write(var='#', color=c, data=res)