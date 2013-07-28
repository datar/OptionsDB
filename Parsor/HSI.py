'''
Created on 2013-4-14

@author: X
'''


import datetime
import re
import os
import DataGettor.URL
import Tools.Log

HSIF_DATA_URL_PATTERN = 'http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsif%s.htm'
HSIF_DATA_COLS = ["Contract Month","AFTER_HOURS_OPEN","*AFTER_HOURS_HIGH","AFTER_HOURS_LOW","AFTER_HOURS_VOLUME","DAY_OPEN","DAY_HIGH","DAY_LOW","DAY_VOLUME","SETTLEMENT","CHANGE_IN_SETTLEMENT","HIGH","LOW","VOLUME","OI","CHANGE_IN_OI"]

HSIO_DATA_URL_PATTERN = 'http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsio%s.htm'
HSIO_DATA_COLS = ["Contract Month","STRIKE_PRICE","CALL_PUT","DAY_OPEN","DAY_HIGH","DAY_LOW","OQP_CLOSE","OQP_CHANGE","IV","VOLUME","OI","CHANGE_IN_OI"] 


HSI_RAW_DATA_ROOT_PATH = "C:\\store\\data\\HSI\\RAW\\"
HSI_CLEAR_DATA_ROOT_PATH = "C:\\store\\data\\HSI\\CLEAR\\"


def HSIFDailyUpdate(dateStr):
    assert dateStr is not None
    Tools.Log.log('Get HSIF info by date ' + dateStr)
    rawContent = getHSIFDataByDate(dateStr)
    if(rawContent is None):
        return
    Tools.Log.log('Get HSIF info size::' + str(len(rawContent)))
    clearContent = parseHSIFRawContent(rawContent)
    Tools.Log.log('Get HSIF clear info %d lines'%(len(clearContent),))
    
    rawContentFilename = HSI_RAW_DATA_ROOT_PATH + 'HSIF.RAW.' + dateStr + '.txt'
    clearContentFilename = HSI_CLEAR_DATA_ROOT_PATH + 'HSIF.CLEAR.' + dateStr + '.txt'

    out = open(rawContentFilename, 'w')
    out.write(rawContent)
    out.close()
    
    lines = []
    lines.append(','.join(HSIF_DATA_COLS))
    for items in clearContent:
        lines.append(','.join(items))
    line = os.linesep.join(lines)
    out = open(clearContentFilename, 'w')
    out.write(line)
    out.close()
    
    
def getHSIFDataByDate(dateStr):
    return getHSIFDataPage(HSIF_DATA_URL_PATTERN % (dateStr)) 

def getHSIFDataPage(url = None):
    return DataGettor.URL.getData(url)

def parseHSIFRawContent(content):
    rawLines = re.split("\n|\r", content)
    count = len(HSIF_DATA_COLS)
    table = []
    for line in rawLines:
        if (re.search("\w{3,3}-\d{2,2}", line) is None):
            continue
        clearLine = line.replace(',', '')
        clearLine = clearLine.replace('+', '')
        items = re.split(" *", clearLine)
        if len(items)==count:
            table.append(items)
    return table


def HSIODailyUpdate(dateStr):
    assert dateStr is not None
    Tools.Log.log('Get HSIO info by date ' + dateStr)
    rawContent = getHSIODataByDate(dateStr)
    if(rawContent is None):
        return
    Tools.Log.log('Get HSIO info size::' + str(len(rawContent)))
    clearContent = parseHSIORawContent(rawContent)
    Tools.Log.log('Get HSIO clear info %d lines'%(len(clearContent),))
    
    rawContentFilename = HSI_RAW_DATA_ROOT_PATH + 'HSIO.RAW.' + dateStr + '.txt'
    clearContentFilename = HSI_CLEAR_DATA_ROOT_PATH + 'HSIO.CLEAR.' + dateStr + '.txt'

    out = open(rawContentFilename, 'w')
    out.write(rawContent)
    out.close()
    
    lines = []
    lines.append(','.join(HSIO_DATA_COLS))
    for items in clearContent:
        lines.append(','.join(items))
    line = os.linesep.join(lines)
    out = open(clearContentFilename, 'w')
    out.write(line)
    out.close()


def getHSIODataByDate(dateStr):
    return getHSIODataPage(HSIO_DATA_URL_PATTERN % (dateStr)) 

def getHSIODataPage(url = None):
    return DataGettor.URL.getData(url)

def parseHSIORawContent(content):
    rawLines = re.split("\n|\r", content)
    count = len(HSIO_DATA_COLS)
    table = []
    for line in rawLines:
        if (re.search("\w{3,3}-\d{2,2}", line) is None):
            continue
        clearLine = line.replace(',', '')
        clearLine = clearLine.replace('+', '')
        items = re.split(" *", clearLine)
        if len(items)==count:
            table.append(items)
    return table


def updateHSIToday():
    dateStr = datetime.datetime.now().strftime('%y%m%d')
    HSIFDailyUpdate(dateStr)
    HSIODailyUpdate(dateStr)

def main():
    updateHSIToday()
        
    
if __name__ == '__main__':
    main()