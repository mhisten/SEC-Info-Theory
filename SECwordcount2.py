import os, sys, csv


path = '/Users/mhisten/Documents/python/SEC/10K/NLTK/Frequencies/'
path1 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/'
os.chdir(path)    
    
for filename in os.listdir(path):
    with open(filename, "r") as f:
        if filename != '.DS_Store':
            cik = filename[:-9]
            print(cik)
            with open(filename) as h:
                count1 = 0
                for row in csv.reader(h):
                    count1 += int(row[1])
            h.close
        outfile = open(path1 + 'WordCount.csv','a')
        outfile.write(str(cik) + ',' + str(count1) + '\n')
