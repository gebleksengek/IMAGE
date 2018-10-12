# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


import requests, re
from assets.warna import *
from assets.fungsi import _headers, write, Request

def cloudflare(website, _verbose=None):
    if _verbose != None:
        write(var='#', color=c, data='cek CloudFlare untuk ' + website)
    combo = ('http://api.hackertarget.com/httpheaders/?q=' + str(website))
    request = Request(combo, _timeout=3, _encode=True)
    if 'cloudflare' in request:
        if _verbose != None:
            write(var='~', color=g, data='CloudFlare ditemukan\n')
            write(var='#', color=y, data='Mencoba untuk di bypass\n')
        req = 'http://www.crimeflare.biz/cgi-bin/cfsearch.cgi'
        pos = {'cfS': website}
        res = requests.post(req, headers=_headers, data=pos).text.encode('utf-8')
        ip_asli = None
        if re.findall(r'\d+\.\d+\.\d+\.\d+', res):
            reg = re.findall(r'\d+\.\d+\.\d+\.\d+', res)
            ip_asli = reg[1]
        else:
            write(var='!', color=r, data='CloudFlare tidak dapat di bypass :(')
        request = Request('http://' + str(ip_asli), _timeout=3, _encode=True)
        if not 'cloudflare' in request.lower():
            if _verbose != None:
                if ip_asli != None:
                    write(var='@', color=c, data='cloudflare dapat di bypass')
                    write(var='~', color=g, data='IP ASLI --> ' + fc + str(ip_asli))
            return(str(ip_asli))
        else:
            if _verbose != None:
                write(var='!', color=r, data='CloudFlare tidak dapat di bypass')
    else:
        if _verbose != None:
            write(var='$', color=b, data=website + ' tidak menggunakan CloudFlare')