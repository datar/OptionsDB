'''
Created on 2013-2-20

@author: CHEN Xing
@contact: chenxing@live.com
'''

import lxml.html
import xml.etree.ElementTree as ET
import DataGettor.URL

ICE_OPTIONS_DATA_PAGE_URL_PATTERN = 'https://www.theice.com/marketdata/reports/icefuturesus/OptionsDailyMarketReport.shtml?tradeDay=%d&tradeMonth=%d&tradeYear=%d&commoditySymbol=%s&venue=%s'

#https://www.theice.com/marketdata/reports/icefuturesus/OptionsDailyMarketReport.shtml?tradeDay=11&tradeMonth=2&tradeYear=2013&commoditySymbol=SO&venue=Electronic
def getPageData(tradeDay, tradeMonth, tradeYear, commoditySymbol, venue='Electronic'):
    url = ICE_OPTIONS_DATA_PAGE_URL_PATTERN % (tradeDay, tradeMonth, tradeYear, commoditySymbol, venue) 
    return DataGettor.URL.getData(url)

def savePageData(data, filename):
    outFile = open(filename, 'w')
    outFile.write(data)
    outFile.close()
    
def parsePageData(data):
    pass

def main():
    #data = getPageData(15, 2, 2013, 'SO')
    #savePageData(data)
    pageData = open('ice_data.txt').read()
    html = lxml.html.fromstring(pageData)
    for e in html:
        print e.tag

if __name__ == '__main__':
    main()