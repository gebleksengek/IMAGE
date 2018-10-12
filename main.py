# -*- coding: utf-8 -*-
"""
Coder: indryanto
"""

from assets import *
from module import Cloudflare, crawl, reverseIP, whoIS, nameServer, cariSubDomain, cariShell, cariAdminPanel, graber

#####################################################################

def InDex():
    try:
        index = raw_input('{cyan}Masukkan nomer: '.format(cyan = c))
        int(index)
        return index
    except ValueError:
        exit(str_Index)
    except KeyboardInterrupt:
        print ''
        exit(write(var='~', color=w, data='Error: User Interrupted'))
    except Exception as e:
        print ''
        exit(write(var='#', color=r, data='Error  ' + str(e)))

def heading(heading, website, color, afterWebHead):
    space = ' ' * 15
    var = str(space + heading + ' \'' + website + '\'' + str(afterWebHead) + " ..." + space)
    length = len(var) + 1
    print ''
    print ('{putih}' + '-' * length + '-').format(putih = w)
    print ('{color}' + var).format(color = color)
    print ('{putih}' + '-' * length + '-').format(putih = w)
    print ''

######################################################################

print Header

######################################################################
try:
    website = raw_input('\n{biru}Masukkan URL untuk di scan {merah}(contoh: smkn2pengasih.sch.id, stewa.org): {kuning}'.format(biru = b, merah = r, kuning = y))
    website = tambahHTTP(website)
except KeyboardInterrupt:
    print ''
    exit(write(var='~', color=w, data='Error: User Interrupted'))
except Exception as e:
    print ''
    exit(write(var='#', color=r, data='Error  ' + str(e)))

print '''
{hijau}Apa yang ingin dilakukan:
1.  Cek CloudFlare
2.  Website Crawler
3.  Reverse IP
4.  whois
5.  NameServer
6.  Cari SubDomain
7.  Shell Finder
8.  Admin Panel Finder
9.  Grab Banner
'''.format(hijau = g)

index = int(InDex())

######################################################################

try:
    if index == 1:
        heading(heading="cek cloudflare untuk ", website=website, afterWebHead='', color=c)
        Cloudflare(website, _verbose=True)
    elif index == 2:
        heading(heading='crawling ', website=website, afterWebHead='', color=c)
        crawl(website)
    elif index == 3:
        heading(heading='Reverse IP ', website=website, afterWebHead='', color=c)
        reverseIP(website)
    elif index == 4:
        heading(heading='whois ', website=website, afterWebHead='', color=c)
        whoIS(website)
    elif index == 5:
        heading(heading='NameServer ', website=website, afterWebHead='', color=c)
        nameServer(website)
    elif index == 6:
        heading(heading='SubDomain ', website=website, afterWebHead='', color=c)
        cariSubDomain(website)
    elif index == 7:
        heading(heading='Cari shell ', website=website, afterWebHead='', color=c)
        cariShell(website)
    elif index == 8:
        heading(heading='Cari admin panel ', website=website, afterWebHead='', color=c)
        cariAdminPanel(website)
    elif index == 9:
        heading(heading='Grab ', website=website, afterWebHead='', color=c)
        graber(website)
    else:
        exit(val_Select)

except KeyboardInterrupt:
    write(var='~', color=w, data='Error: User Interrupted')

except Exception as e:
    write(var='#', color=r, data='Error  ' + str(e))

######################################################################

print Footer
