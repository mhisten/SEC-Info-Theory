import sys, os, codecs, nltk
from nltk.stem import WordNetLemmatizer
	
path1 = '/Users/mhisten/Documents/python/SEC/second regression/3sic/libraries/'
path2 = '/Users/mhisten/Documents/python/SEC/second regression/3sic/fdist/'
os.chdir(path1)

for filename in os.listdir(path1):
    with open(filename, "r") as f:
        if filename != '.DS_Store':
            sic = filename[:4]
            print(sic)
            f=open(filename, "r")
            f = f.read
            f = f()
            f = f.lower()
            f = str(f)

            word_tokens = nltk.word_tokenize(f)
            fdist1 = nltk.FreqDist(word_tokens)
            y = fdist1.most_common(len(fdist1))
            #fdist1.plot(40)

            for i in y: 
                outfile = open(path2 + str(sic) + 'fdist.csv','a')
                outfile.write(str(i[0]) + ',' + str(i[1]) + '\n')

