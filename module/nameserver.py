# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


from assets.warna import *
from assets.fungsi import write, hapusHTTP, tambahHTTP
from dns.resolver import query

def nameServer(website):
    website = hapusHTTP(website)
    res = query(website, 'NS')
    for nameserver in res:
        write(var='#', color=c, data=nameserver)