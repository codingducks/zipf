import  collections, string, csv

name = input('enter a file->')
handle = open(name,  'r')
table = str.maketrans('','',string.punctuation)
text = handle.read().lower()
text = text.translate(table)
words = text.split()


x = collections.Counter(words)



print (x.most_common())

filename = input('namethis.csv-->')

with open(filename, 'w') as resultFile:
    writer = csv.writer(resultFile)
    for row in x.most_common():
        writer.writerow(row)
'''
import pprint

resultFile = open(filename, 'w')
resultFile.write(pprint.pformat(x.most_common()))
resultFile.close()
'''
