from bs4 import BeautifulSoup
import requests, sys, os, codecs, csv, urllib2

path = '/Users/mhisten/Documents/python/SEC/10K'
os.chdir(path)
f = codecs.open('10-Klink1.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    print cik
    url = row[1]
    doc_resp = requests.get(url)
    doc_str = doc_resp.text

    soup = BeautifulSoup(doc_str, 'html.parser')
    tags = soup.find_all('a', href=True)
    x = 0
    for tag in tags:
        if x == 1: #End loop after finding link
            break
        if 'ITEM' in tag.text:
            search = tag.text
            item = tag.text.encode('utf-8').strip()
            item = item.replace(' ','')
            if '1' in item:
                link = url + tag['href']
                x = 1
                break

    if x == 0:
        outfile = open(path + '/links/' '10-KBusExcept.csv','a')
        outfile.write(str(cik) + ',' + url + '\n')
    else:
        outfile = open(path + '/links/' '10-KBusiness.csv','a')
        outfile.write(str(cik) + ',' + link + '\n')





        






