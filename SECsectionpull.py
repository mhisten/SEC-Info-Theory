from bs4 import BeautifulSoup
import os, sys, csv, re, urllib2, csv, codecs, requests

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
    page = response.read()
    
    page = page.strip()
    page = page.replace('\n', ' ') #<===replace the \n (new line) character with space
    page = page.replace('\r', '') #<===replace the \r (carriage returns -if you're on windows) with space
    page = page.replace('&nbsp;', ' ') #<===replace "&nbsp;" (a special character for space in HTML) with space. 
    page = page.replace('&#160;', ' ') #<===replace "&#160;" (a special character for space in HTML) with space.
    while '  ' in page:
        page = page.replace('  ', ' ') #<===remove extra space


    regexs = ('bold;\">\s*Item 1\.(.+?)bold;\">\s*Item 1A\.',  #second item tells you where to end
            'b>\s*Item 1\.(.+?)b>')           

    for regex in regexs:
        match = re.search (regex, page, flags=re.IGNORECASE)

        if match:
            soup = BeautifulSoup(match.group(1), "html.parser") #<=== match.group(1) returns the texts inside the parentheses (.*?) 
            rawText = soup.text.encode('utf8') #<=== you have to change the encoding the unicodes
            outText = re.sub("^business\s*","",rawText.strip(),flags=re.IGNORECASE)
            print outText

            break




