'''
Created on 2013-4-14

@author: X
'''


import datetime
import re
import DataGettor.URL

HSIF_DATA_URL_PATTERN = 'http://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsif%s.htm'
HSIF_DATA_COLS = ["Contract Month","AFTER_HOURS_OPEN","*AFTER_HOURS_HIGH","AFTER_HOURS_LOW","AFTER_HOURS_VOLUME","DAY_OPEN","DAY_HIGH","DAY_LOW","DAY_VOLUME","SETTLEMENT","CHANGE_IN_SETTLEMENT","HIGH","LOW","VOLUME","OI","CHANGE_IN_OI"]
HSI_RAW_DATA_ROOT_PATH = ""
HSI_CLEAR_DATA_ROOT_PATH = ""


def HSIFDailyUpdate(dateStr = None):
    if dateStr is None :
        dateStr = datetime.date.today().strftime('%y%m%d')
    rawContent = getHSIFDataByDate(dateStr)
    
    
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

def main():
    dateStr = '130412'
    table = parseHSIFRawContent(getHSIFDataByDate(dateStr))
    print table
    
if __name__ == '__main__':
    main()