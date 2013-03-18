'''
Created on 2013-3-18

@author: CHEN Xing
@contact: chenxing@live.com
'''

import urllib2

def getData(url):
    return urllib2.urlopen(url).read()