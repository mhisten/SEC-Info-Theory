import sys, os, codecs, csv
	
path = '/Users/mhisten/Documents/python/SEC/second regression/4sic/'
path1 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/fdist/'
path2 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/Frequencies/'
path3 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/encoded/'

os.chdir(path)
f = codecs.open('4Siclist.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    sic = row[0]
    print(sic)

    lib = str(sic) + 'fdist.csv'

    #Open library distribution
    os.chdir(path1)
    with open(lib, 'r') as f:
        reader = csv.reader(f)
        fdistlib = list(reader)

    #Huffman encoding
    y = 0
    B = []
    for i in fdistlib:
        x = i[1]
        x = int(x)
        y = y + x

    A0 = []
    A1 = []
    A2 = []

    for i in fdistlib: #Set matrix 1 for probability combinations
        i = (*i, int(i[1])/y, 0)
        A0.append(i)
        A1.append(i)
    for i in fdistlib: #Set matrix 2 for tracking
        i = list(i)
        i = (*i, 0, 0)
        A2.append(i)

    while len(A1) > 2:
        A1 = sorted(A1, key = lambda x: x[2], reverse=True)
        last = A1[-2:]
        last = sorted(last, key = lambda x: x[0])
        secondlast = (last[-2])
        firstlast = (last[-1])
        #Merge last two rows and sum probabilities and increase bit
        prob = secondlast[-2] + firstlast[-2]
        secondlast = list(secondlast)
        secondlast[-2] = prob
        A1[-2] = secondlast
        A1 = A1[:-1] #remove last row

        bumped = firstlast[0] #track removed row
        merged = secondlast[0] #track envelopment under

        count = 0
        for i in A2:
            i = list(i)
            if i[0] == bumped:
                i[3] = i[3] + 1
                i[2] = merged
            if i[0] == merged:
                i[3] = i[3] + 1
            if i[2] == bumped:
                i[2] = merged
            if i[2] == merged:
                i[3] = i[3] + 1
            A2[count] = i
            count = count + 1

    winner1 = list(A1[0])
    winner2 = list(A1[1])

    count = 0
    for i in A2:
        i = list(i)
        if i[0] == winner1[0]:
            i[3] = i[3] + 1
        if i[0] == winner2[0]:
            i[3] = i[3] + 1
        A2[count] = i
        count = count + 1

    L = []
    for i in A2:
        j = i[0]
        k = i[3]
        l = (j,k)
        L.append(l)

    count = 0
    z2 = 0
    for i in A2:
        j = A0[count]
        z1 = i[3] * j[2]
        z2 = z2 + z1
        count = count + 1

    outfile = open(path3 + str(sic) + 'Encoded.csv','a')
    outfile.write(str('#hoffman') + ',' + str(z2) + '\n')

    for i in L: 
        outfile = open(path3 + str(sic) + 'Encoded.csv','a')
        outfile.write(str(i[0]) + ',' + str(i[1]) + '\n')

