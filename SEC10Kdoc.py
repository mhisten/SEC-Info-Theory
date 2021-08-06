from bs4 import BeautifulSoup
import requests
import sys
import os
import codecs
import csv

# Format file
path = '/Users/mhisten/Documents/python/SEC/'
os.chdir(path)
f = codecs.open('10-K2.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    print cik
    url = row[1]

    # Obtain HTML for document page
    doc_resp = requests.get(url)
    doc_str = doc_resp.text

    # Find the doc link
    soup = BeautifulSoup(doc_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile', summary='Document Format Files')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 3:
            if '10-K' in cells[3].text:
                doc_link = 'https://www.sec.gov' + cells[2].a['href']
                filetype = doc_link[-3:]
                if filetype == 'htm':
                    outfile = open(path + '/10K/' + '10-Klink.csv','a')
                    outfile.write(str(cik) + ',' + doc_link + '\n')
                else:
                    outfile = open(path + '/10K/Exceptions/' + '10-Klinke.csv','a')
                    outfile.write(str(cik) + ',' + doc_link + '\n')
        






