from bs4 import BeautifulSoup
import requests
import sys
import os
import codecs

path = '/Users/mhisten/Documents/python/SEC/'
os.chdir(path)

# Access page
type = '10-K'
dateb = '20171231'

f = codecs.open('SEClist2.csv', 'r', 'utf-8-sig')

#with open('Company List1.csv', mode = 'r', encoding = 'utf-8-sig') as f:
for line in f:
    cik = line.strip() #Company
    print cik

    # Obtain HTML for search page
    base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}&dateb={}"
    edgar_resp = requests.get(base_url.format(cik, type, dateb)) #Link to 10-K search
    edgar_str = edgar_resp.text
    
    doc_link = cik

    soup = BeautifulSoup(edgar_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile2')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 3:
            if '10-K/A' in cells[0].text:
                pass
            else:
                if '2017' in cells[3].text:
                    doc_link = 'https://www.sec.gov' + cells[1].a['href']
                    outfile = open(path + '10-K1.csv','a')
                    outfile.write(str(cik) + '\n')
                    outfile = open(path + '10-K.csv','a')
                    outfile.write(str(cik) + ',' + doc_link + '\n')

        else:
            outfile = open(path + 'No10-K1.csv','a')
            outfile.write(str(cik) + '\n')

    with open('10-K1.csv','r+') as source:
        filter_lines = source.readlines()

    with open('No10-K1.csv','r') as f:
        lines = f.readlines()

    with open('No10-K.csv', 'w') as target:
        for line in lines:
            if line not in filter_lines:
                target.write(line)

os.remove('No10-K1.csv')  
os.remove('10-K1.csv')  