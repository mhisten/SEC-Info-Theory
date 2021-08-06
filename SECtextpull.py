
import os, sys, csv, re, urllib2, csv, codecs, requests

path = '/Users/mhisten/Documents/python/SEC/10K/links/Exceptions3/'
path1 = '/Users/mhisten/Documents/python/SEC/10K/links/MDA3/'
path2 = '/Users/mhisten/Documents/python/SEC/10K/links/'
os.chdir(path)

regexs = ("Item 7.&#xA0;Management(.*)Item 8",
"Item 7.&#xA0;  Management(.*)Item 8.",
"Item 7.&#xA0;   Management(.*)Item 8.",
"Item 7.&#xA0;    Management(.*)Item 8.",
"Item 7.&#xA0;     Management(.*)Item 8.")

for filename in os.listdir(path):
    with open(filename, "r") as f:
        cik = filename[:-4]
        print cik
        f = f.read()
        x = 0
        for regex in regexs:
            match = re.search (regex, f, flags=re.IGNORECASE)
            if match:
                g = match.group(1)
                g = 'Managements' + g
                outfile = open(path1 + str(cik) + '.txt','a')
                outfile.write(g)
                os.remove(str(cik) + '.txt')
                x = 1
                break

    if x == 0:
        outfile = open(path2 + 'MDAexceptions2.csv','a')
        outfile.write(str(cik) + '\n')


