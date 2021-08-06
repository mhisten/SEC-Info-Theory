import os, sys, csv, re, urllib2, csv, codecs, requests

path = '/Users/mhisten/Documents/python/SEC/10K/links/Exceptions1/'
path1 = '/Users/mhisten/Documents/python/SEC/10K/links/Exceptions2/'
os.chdir(path)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

for filename in os.listdir(path):
    with open(filename, "r") as f:
		cik = filename[:-4]
		print cik
		f = f.read()
		cleanr = cleanhtml(f)
		words = cleanr.split()

		if len(words) > 15000:
			y = str(cleanr)
			y = y[15000:]
			outfile = open(path1 + str(cik) + '.txt','a')
			outfile.write(y)
		else:
			print 'hi'
			outfile = open(path + 'Exceptions11.csv','a')
			outfile.write(str(cik) + ',' + str(len(words)) + '\n')
			print 'bye'


			
