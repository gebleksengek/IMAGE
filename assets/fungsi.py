# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""


from assets.warna import *
import requests
import re

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

website_kosong = '\n\t{merah}[X] Tolong masukkan URL Website :(\n'.format(merah = r)

URL_salah = '\n\t{merah}[X] Tolong masukkan URL yang benar (contoh: google.com, stewa.org) :(\n'.format(merah = r)

str_Index = '\n\t{merah}[X] Tolong masukkan nomer (contoh: 1, 2, 3, 4) :(\n'.format(merah = r)

val_Select = '\n\t{merah}[X] Tolong nomer seperti dalam daftar :(\n'.format(merah = r)

def cekWebNotEmpty(website):
    if len(website) >= 1:
        return 'valid'
    else:
        return '!valid'

def cekWebBenar(website):
    web = cekWebNotEmpty(website)
    if web is 'valid':
        if not (re.match(r'(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)', website)):
            exit(URL_salah)
    else:
        exit(website_kosong)

def hapusURL(website):
    web = cekWebBenar(website)
    website = website.replace('http://', '')
    website = website.replace('http://www.', '')
    website = website.replace('https://', '')
    website = website.replace('https://www.', '')
    website = website.replace('www.', '')
    return(website)

def hapusHTTP(website):
    website = hapusURL(website)
    return(website)

def tambahHTTP(website):
    website = hapusURL(website)
    website = ('http://' + website)
    return(website)

def write(var, color, data):
    if var == None:
        print color + str(data)
    elif var != None:
        print ('{putih}[{hijau}' + var + '{putih}] ' + color + str(data)).format(putih = w, hijau = g)

def Request(website, _timeout=None, _encode=None):
    try:
        if _encode == None:
            return requests.get(website, headers=_headers, timeout=_timeout).content
        elif _encode == True:
            return requests.get(website, headers=_headers, timeout=_timeout).text.encode('utf-8')
    except requests.exceptions.MissingSchema:
        pass
    except requests.exceptions.ContentDecodingError:
        pass
    except requests.exceptions.ConnectionError:
        return fg + sb + '\n Error: Website Salah / Website Down'
        pass
    except Exception as e:
        return fc + sb + 'Error: ' + fg + sb + str(e)
        pass
