

# - - - Lê as tarefas, executa as remoções e as salva na pasta tt/ com mesmo nome.

from __future__ import print_function, unicode_literals
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import os
import glob
import time
import nltk
import re
import pprint
from nltk import word_tokenize
from unicodedata import normalize
path = 'textos/'

# remover plurais
def stem(txt):
    stemmer = SnowballStemmer("portuguese")
    # txt = word_tokenize(txt)
    filt_stem = []

    for i in word_tokenize(txt):
        filt_stem.append(stemmer.stem(i))

    return filt_stem

# Remover acentos de um determinado texto
def remove_accent(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def remove_stopwords(txt):
    from nltk.corpus import stopwords
    #stopwords = open('stopwords.txt','r',encoding='ISO-8859-1')
    filtrado = [w for w in word_tokenize(txt) if not w in stopwords.words('portuguese')]
    #filtrado = [w for w in word_tokenize(txt) if not w in stopwords]
    return filtrado

# text = open('textos/2669', 'r', encoding='utf-8').read()
# print(text)
# print(remove_stopwords(text))

def remove_specialChar(txt):
    specialChars = ['.', ',', '!', '?', ';', "'", '"', ':', '/', '|', "\\", '(', ')', '[', ']', '{', '}','-','#','*','@', '=', '#', '$', '%', '>','<']
    for char in specialChars:
        txt = txt.replace(char, '')
    return txt

def remove_double_spaces(txt):
    return re.sub(' +', ' ',txt)

# contador de tempo
start = time.time()
i = 0
for filename in glob.glob(os.path.join(path, '*')):
    textwords = open(filename, 'r', encoding='utf8').read()
    print(textwords)
    print('#', filename)
    print(type(textwords))


    newFilename = "new%s" % filename
    newFile = open(newFilename,'w')
    textwords = remove_specialChar(textwords)

    textwords = remove_double_spaces(textwords)
    textwords = remove_accent(textwords)

    textwords = stem(textwords)

    textwords = remove_stopwords(textwords)
    textwords2 = ' '.join(textwords)
    textwords = textwords2


    newFile.write(textwords)

end = time.time()
print("\n tempo total:\n")
print(end-start)





