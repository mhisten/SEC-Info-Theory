from bs4 import BeautifulSoup
import requests
import sys
import os
import codecs
import csv

# Format file
path = '/Users/mhisten/Documents/python/SEC/'
os.chdir(path)
f = codecs.open('10-K.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    print cik
    url = row[1]

    # Obtain HTML for document page
    doc_resp = requests.get(url)
    doc_str = doc_resp.text


    # Find the XBRL link
    xbrl_link = ''
    soup = BeautifulSoup(doc_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile', summary='Data Files')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 3:
            if 'INS' in cells[3].text:
                xbrl_link = 'https://www.sec.gov' + cells[2].a['href']

    # Obtain XBRL text from document
    xbrl_resp = requests.get(xbrl_link)
    xbrl_str = xbrl_resp.text
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all()


    contexts = {}

    for tag in tag_list:
        if tag.name == 'xbrli:context':
            
            #This section of code finds the start date of the context if it exists.
            start_date_tag = tag.find(name = 'xbrli:startdate')
            if start_date_tag == None:
                start_date = None
            else:
                start_date = start_date_tag.text
            
            #This section of code finds the end date of the context if it exists.
            end_date_tag = tag.find(name = 'xbrli:enddate')
            if end_date_tag == None:
                end_date = None
            else:
                end_date = end_date_tag.text
                date = end_date_tag.text
                datetype = 'period'
                
            #This section of code finds the instant date of the context if it exists.
            instant_date_tag = tag.find(name = 'xbrli:instant')
            if instant_date_tag != None:
                date = instant_date_tag.text
                datetype = 'instant'
            
            #build a dictionary of date information within a dictionary of context titles
            dtinfo = {'date' : date, 'year' : date[0:4], 'datetype' : datetype, 'startdate' : start_date, 'enddate' : end_date}
            contexts[tag.attrs['id']] = dtinfo
            
    # Find and print stockholder's equity
    X = []
    for tag in tag_list:
        if tag.name == 'us-gaap:stockholdersequity':
            year = contexts[tag.attrs['contextref']]['year']
            if year == '2016':
                x = [int(tag.text)]
                X[1:1] = x
    if len(X)>0:   
        stockholdersequity = max(X)

    # Find and print assets
    Y = []
    for tag in tag_list:
        if tag.name == 'us-gaap:assets':
            year = contexts[tag.attrs['contextref']]['year']
            if year == '2016':
                y = [int(tag.text)]
                Y[1:1] = y
    if len(Y)>0:   
        assets = max(Y)

    outfile = open(path + 'Controls/' + 'controls.csv','a')
    outfile.write(str(cik) + ',' + str(assets) + ',' + str(stockholdersequity) + '\n')


    




