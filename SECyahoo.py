from yahoofinancials import YahooFinancials
import ssl, os, csv, sys, codecs


path = '/Users/mhisten/Documents/python/SEC/10K/Controls/'
ssl._create_default_https_context = ssl._create_unverified_context

os.chdir(path)
f = codecs.open('data2.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    cik = row[0]
    print(cik)
    ticker = row[1]
    ticker = str(ticker)
    print(ticker)
    try:
        yahoo_financials = YahooFinancials(ticker)
        x = yahoo_financials.get_financial_stmts('annual','balance')
        y = x.items()
        z = str(y)
        beg = z.find("{'2016")
        end = z.find("{'2015")

        a = z[beg:end] #Year string
        #Liab
        beg = a.find('totalLiab')
        b = a[beg:]
        beg1 = b.find(":")
        end1 = b.find(',')
        liab = b[(beg1+2):end1]

        #Assets
        beg = a.find('totalAssets')
        b = a[beg:]
        beg1 = b.find(":")
        end1 = b.find(',')
        assets = b[(beg1+2):end1]

        outfile = open(path + 'Controls1.csv','a')
        outfile.write(str(cik) + ',' + str(ticker) + ',' + str(assets) + ',' + str(liab) + '\n')

    except:
        outfile = open(path + 'ControlsExceptions.csv','a')
        outfile.write(str(cik) + ',' + str(ticker) + '\n')
        


