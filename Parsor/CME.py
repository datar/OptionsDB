'''
Created on 2013-7-28

@author: X
'''

import datetime
import re
import os
import DataGettor.URL
import Tools.Log

COMEX_DATA_TXT_URL = 'ftp://ftp.cmegroup.com/settle/stlcomex'
COMEX_FUTURE_DATA_CSV_URL = 'ftp://ftp.cmegroup.com/pub/settle/comex_future.csv'
COMEX_OPTION_DATA_CSV_URL = 'ftp://ftp.cmegroup.com/pub/settle/comex_option.csv'

NYMEX_DATA_TXT_URL = 'ftp://ftp.cmegroup.com/pub/settle/stlnymex'
NYMEX_FUTURE_DATA_CSV_URL = 'ftp://ftp.cmegroup.com/pub/settle/nymex_future.csv'
NYMEX_OPTION_DATA_CSV_URL = 'ftp://ftp.cmegroup.com/pub/settle/nymex_option.csv'

CME_RAW_DATA_ROOT_PATH = "C:\\store\\data\\HSI\\RAW\\"
CME_CLEAR_DATA_ROOT_PATH = "C:\\store\\data\\HSI\\CLEAR\\"

def CMEDailyUpdate(dateStr):
    assert dateStr is not None
    Tools.Log.log('Get COMEX info by date ' + dateStr)
    rawContent = DataGettor.URL.getData(COMEX_DATA_TXT_URL)
    if(rawContent is None):
        return
    Tools.Log.log('Get COMEX info size::' + str(len(rawContent)))
    #clearContent = parseHSIFRawContent(rawContent)
    #Tools.Log.log('Get HSIF clear info %d lines'%(len(clearContent),))
    
    rawContentFilename = CME_RAW_DATA_ROOT_PATH + 'COMEX.RAW.' + dateStr + '.txt'
    #clearContentFilename = HSI_CLEAR_DATA_ROOT_PATH + 'HSIF.CLEAR.' + dateStr + '.txt'

    out = open(rawContentFilename, 'w')
    out.write(rawContent)
    out.close()
    
    #===========================================================================
    # lines = []
    # lines.append(','.join(HSIF_DATA_COLS))
    # for items in clearContent:
    #    lines.append(','.join(items))
    # line = os.linesep.join(lines)
    # out = open(clearContentFilename, 'w')
    # out.write(line)
    # out.close()
    #===========================================================================
    
def getCMEDataPage(url = None):
    return DataGettor.URL.getData(url)


def main():
    CMEDailyUpdate('210130726')

if __name__ == '__main__':
    main()
