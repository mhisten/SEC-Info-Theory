from sklearn.feature_extraction.text import TfidfVectorizer
import sys, os, codecs, csv

path1 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/MDAclean2/'
path2 = '/Users/mhisten/Documents/python/SEC/second regression/4sic/'

os.chdir(path2)
f = codecs.open('4Data2.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')
os.chdir(path1)

for row in reader:
    cik = row[0]
    sic = row[1]
    print(cik)

    filename1 = str(cik) + '.txt'
    filename2 = str(sic) + 'library.txt'

    text_files = [filename1, filename2]
    documents = [open(f).read() for f in text_files]
    tfidf = TfidfVectorizer().fit_transform(documents)
    # no need to normalize, since Vectorizer will return normalized tf-idf
    pairwise_similarity = tfidf * tfidf.T
    x = pairwise_similarity[0]
    y = x[0,:].toarray()
    z = (y[:,1])

    outfile = open(path2 + '4Cosine.csv','a')
    outfile.write(str(cik) + ',' + str(z) + '\n')