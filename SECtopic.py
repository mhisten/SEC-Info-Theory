from bs4 import BeautifulSoup
import requests
import sys
import os
import codecs
import csv
import urllib2

# Format file

path = '/Users/mhisten/Documents/python/SEC/10K'
os.chdir(path)
f = codecs.open('10-Klink1.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    print cik
    url = row[1]
    print url

    response = urllib2.urlopen(url)
    
    #words: list of uncertainty words from Loughran and McDonald (2011)
    words = ['anticipate', 'believe', 'depend', 'fluctuate', 'indefinite', 'likelihood', 'possible', 'predict', 'risk', 'uncertain']
    count = {}
    for elem in words:
        count[elem] = 0
    for line in response:  
        elements = line.split()  
        for word in words:     
            count[word] = count[word] + elements.count(word)

    print(count)
        






