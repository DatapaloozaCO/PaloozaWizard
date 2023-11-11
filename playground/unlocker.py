#!/usr/bin/env python
print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
    '$ sudo pip install six')
print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
    'YOURPASS, please contact sales@brightdata.com')
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
if sys.version_info[0]==2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler(
            {'http': 'http://brd-customer-hl_ab2b430b-zone-unblocker:g7vui7owe35t@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_ab2b430b-zone-unblocker:g7vui7owe35t@brd.superproxy.io:22225'}))
    print(opener.open('http://lumtest.com/myip.json').read())
if sys.version_info[0]==3:
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {'http': 'http://brd-customer-hl_ab2b430b-zone-unblocker:g7vui7owe35t@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_ab2b430b-zone-unblocker:g7vui7owe35t@brd.superproxy.io:22225'}))
    print(opener.open('https://www.amazon.com/Legend-Zelda-Breath-Wild-Nintendo-Switch/dp/B097B2YWFX/ref=sr_1_2?crid=AMBZI2YGNFC3&keywords=zelda%2Bvideo%2Bgame&qid=1698834691&sprefix=zelda%2Bvideogame%2Caps%2C241&sr=8-2&th=1').read())