import sys, os, codecs, nltk
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
	
path1 = '/Users/mhisten/Documents/python/SEC/10K/NLTK/MDAclean/'
os.chdir(path1)

filename = "745981.txt"


with open(filename, "r") as f:
    f=open(filename, "r")
    f = f.read
    f = f()
    f = str(f)

    word_tokens = nltk.word_tokenize(f)
    fdist1 = nltk.FreqDist(word_tokens)
    y = fdist1.most_common(32)

    x_data = []
    y_data = []

    for i in y:
        x = i[0] 
        y = i[1]
        if x != "loan":
            if x != "total":
                if x == "loans":
                    x = "loan"

                x_data.append(x)
                y_data.append(y)

    plt.plot(x_data, y_data)
    plt.xticks(rotation=90)
    plt.ylabel('Word Count')
    plt.title('Banking')
    plt.tight_layout()
    plt.show()