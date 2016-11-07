#!/usr/bin/env python
# coding=utf-8

# - - - Lê as tarefas, executa as remoções e as salva na pasta tt/ com mesmo nome.

import os
import glob
import time
import nltk
import re
import pprint
from nltk import word_tokenize
from unicodedata import normalize
from nltk.corpus import stopwords
path = 'tt/'

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def remove_double_spaces(txt):
    return re.sub(' +', ' ',txt)

start = time.time()

stopwords = open('stop2.txt', 'r', encoding='utf8').read().split()
stopwords.append(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','-','#','*',])

pontos = ['.','•','‘','’','“','”','–', ',', '!', '?', ';', "'", '"', ':', '/', '|', "\\", '(', ')', '[', ']', '{', '}','#','*','@', '=', '#', '$', '%', '>','<']

# tokens = word_tokenize(stopwords,language='portuguese')
# print(tokens)

for filename in glob.glob(os.path.join(path, '*')):
    textwords = open(filename, 'r', encoding='utf8').read().split()
    novo = "n%s" % filename
    t2 = open(novo,'w', encoding='utf8')

    for t in textwords:
        filteredtext = [t.lower() for t in textwords if t.lower() not in stopwords]

    # Gravando o texto no arquivo... Solução muito burra
    #ini = time.time()

    texto = ''
    for x in filteredtext:
        texto = '%s %s ' % (texto, x)
    texto = texto[1:]

    for p in pontos:
        texto = texto.replace(p, ' ')
    texto = texto.replace("-", " ")

    #texto = remover_acentos(texto)

    texto = remove_double_spaces(texto)

    t2.write(texto)
    matriz.append(texto)




print(matriz)
end = time.time()
print("\n tempo total:\n")
print(end-start)





