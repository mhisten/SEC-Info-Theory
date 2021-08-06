
import os, sys, csv, codecs

path = '/Users/mhisten/Documents/python/SEC/second regression/4sic/'
path1 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/libraries/'
path2 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/MDAclean/'

os.chdir(path)
f = codecs.open('4Data.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    sic = row[1]
    print(cik)
    filename = str(cik) + '.txt'
    os.chdir(path2)
    with open(filename, "r") as g:
        g = g.read()
        g = g + ' '
        outfile = open(path1 + str(sic) + 'library.txt','a')
        outfile.write(g)