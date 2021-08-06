
import urllib2
from bs4 import BeautifulSoup
import requests
import os
import numpy as np


path = '/Users/mhisten/Documents/python/SEC'
#You need to selection your path
file1 = 'Exceptions.txt'
#You need to name your files
os.chdir(path)
opener = urllib2.build_opener()
page1 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='
page2 = '&type=10-k&dateb=20061231&owner=exclude&count=40'
page3 = 'https://www.sec.gov'

with open('Company List.txt') as f:
    try:    
        for line in f:
            Company = line.strip()
            url = (str(page1) + str(Company) + str(page2))

            ourUrl = opener.open(url).read()
            print ourUrl
            #need to kick out empty search results
            link = ourUrl[ourUrl.find('<td nowrap="nowrap">10-K</td>'):]
            soup = BeautifulSoup(link, "lxml")
            link1 = soup.find('a')['href']
            url = page3 + link1 #Link to 10-K search


            try:
                ourUrl = opener.open(url).read()
                link = ourUrl[ourUrl.find('<table class="tableFile" summary="Document Format Files">'):]
                soup = BeautifulSoup(link, "lxml")
                link1 = soup.find('a')['href']
                url = page3 + link1 #Link to 10-K document

                print Company

            except:
                print Company

    except:
        print Company
        outfile = open(path + '/' + file1,'a')
        outfile.write(str(Company) + '\n')

                

