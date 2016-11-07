# coding=utf-8

# Importação das Bibliotecas
from __future__ import print_function, unicode_literals
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import os
import time
import glob
import nltk
import re
from unicodedata import normalize
from nltk.corpus import stopwords
path = 'ntt/'

stemmer = SnowballStemmer("portuguese")

# matriz de palavras

col = word_tokenize(open('colunas_fixo','r',encoding='utf8').read())
print(col)

matrizA = col

for filename in glob.glob(os.path.join(path, '*')):
    matrizB = []
    fdist = open(filename, 'r', encoding='utf8').read()
    fdist = nltk.FreqDist(fdist)
    print(fdist)
    for i in col:
        if i in fdist:
            x = str(fdist[i])

            matrizB.append(x.zfill(4))
        else:
            matrizB.append('0000')
    matrizA.append(matrizB)

print(matrizA)

# transformar a lista acima em uma única linha da matriz
line = ''
for x in matrizA:
    line = line+x

print(line)
# for t in textwords:
#     filteredtext = [t.lower() for t in textwords if t.lower() not in stopwords]
