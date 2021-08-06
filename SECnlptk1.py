import sys, os, codecs, nltk, csv
from nltk.stem import WordNetLemmatizer
	
path = '/Users/mhisten/Documents/python/SEC/10K/NLTK/'
path1 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/MDAclean/'
path2 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/Frequencies/'


os.chdir(path)
g = codecs.open('DataAll.csv', 'r', 'utf-8-sig')
reader = csv.reader(g, delimiter=',')

for row in reader:
    cik = row[0]
    print(cik)
    filename = str(cik) + '.txt'

    os.chdir(path1)
    with open(filename, "r") as f:
        f = f.read
        f = f()
        f = f.lower()
        f = str(f)

        word_tokens = nltk.word_tokenize(f)

        fdist1 = nltk.FreqDist(word_tokens)
        y = fdist1.most_common(len(fdist1))
        #fdist1.plot(40)

        for i in y: 
            outfile = open(path2 + str(cik) + 'fdist.csv','a')
            outfile.write(str(i[0]) + ',' + str(i[1]) + '\n')
