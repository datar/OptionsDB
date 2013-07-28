'''
Created on 2013-3-18

@author: CHEN Xing
@contact: chenxing@live.com
'''

import urllib2
import Tools.Log

def getData(url):
    try:
        result = urllib2.urlopen(url).read()
        Tools.Log.log('Get %d bits msg from %s'%(len(result), url))
    except (urllib2.HTTPError,urllib2.urlopen):
        result = None
        Tools.Log.log('Get sth wrong from %s'%(url,))
    return result