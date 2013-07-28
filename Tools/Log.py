'''
Created on 2013-7-22

@author: X
'''

import datetime
import os

DEFAULT_LOG_FILE_NAME = 'log.'+datetime.date.today().strftime('%Y%m%d')+'.txt'

def log(msg, filename = DEFAULT_LOG_FILE_NAME):
    out = open(filename, 'a')
    out.write(str(datetime.datetime.now()))
    out.write('::')
    out.write(msg)
    out.write(os.linesep)
    out.close()