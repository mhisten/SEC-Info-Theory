import sys, os, codecs, csv
	
path = '/Users/mhisten/Documents/python/SEC/second regression/4sic/'
path1 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/encoded/'
path2 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/Frequencies/'
path3 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/encoded/'

os.chdir(path)
f = codecs.open('4Data2.csv', 'r', 'utf-8-sig') 
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    sic = row[1]
    print(cik)

    filename = str(cik) + 'fdist.csv'
    lib = str(sic) + 'Encoded.csv'

    #Open library distribution for bit assignments
    os.chdir(path1)
    with open(lib, 'r') as g:
        reader = csv.reader(g)
        fdistlib = list(reader)
        entropymax = fdistlib[-1]
        entropymax = entropymax[1] #maximum value in library
        entropylib = (fdistlib[0])
        entropylib = entropylib[1] #hoffman of library
        fdistlib1 = ([x for x,_ in fdistlib])
    g.close()

    #Get total frequency for entropy calculation
    os.chdir(path2)
    with open(filename) as h:
        count1 = 0
        for row in csv.reader(h):
            count1 += int(row[1])
    h.close

    i = codecs.open(filename, 'r', 'utf-8-sig')
    reader1 = csv.reader(i, delimiter=',')
    entropycik = 0
    for j in reader1:
        token = j[0]
        freq = j[1]
        prob = int(j[1])/count1 #probability of word
        try:
            ll = (fdistlib1.index(token))
            k = fdistlib[ll] #information content of word
        
        except: #if word does not appear in huffman library,
            k = [token, entropymax] #take max value

        entropycik = int(k[1])*prob + entropycik

    i.close() 

    outfile = open(path + 'Entropy.csv','a')
    outfile.write(str(cik) + ',' + str(entropylib) + ',' + str(entropycik) + ',' + str(count1) + '\n')
