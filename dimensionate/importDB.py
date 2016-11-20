#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import pymysql
import re
import string
import os
import time
import glob
import nltk
from nltk.corpus import stopwords
from unicodedata import normalize

start = time.time()

#------------------ cleanText    ------------------#
def cleanText(sentence):
    def remover_acentos(sentence):
        return normalize('NFKD', sentence).encode('ASCII', 'ignore').decode('ASCII')

    def remove_stopwords(sentence):
        return [token for token in nltk.word_tokenize(sentence) if token.lower() not in stopwords.words('portuguese')]

    def remove_punctuation_old(sentence):
        pontos = ['.', '•', '‘', '’', '“', '”', '–', ',', '!', '?', ';', "'", '"', ':', '/', '|', "\\", '(', ')', '[', ']', '{', '}', '#', '*', '@', '=', '#', '$', '%', '>', '<']
        for p in pontos:
            txt = sentence.replace(p, ' ')
        return sentence.replace("-", " ")

    def remove_punctuation(sentence):
        return re.sub('[%s]' % re.escape(string.punctuation), ' ', sentence)

    def remove_lines(sentence):
        regex = re.compile(r'[\n\r\t\x90\x91\x92\x93\x94\x95\x96\x97\x98]')
        return regex.sub(" ", sentence)

    return remove_stopwords(remove_punctuation(remove_lines(sentence)))

#------------------ importDB     ------------------#

def importDB(command):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='bitnami_redmine')
    cur = conn.cursor()
    cur.execute(command)

    cats = open("cats.txt", "w", encoding='utf8')
    lines = []

    def cleanRow(row):
        clean = str(row)
        return clean[1:(len(clean) - 2)]

    for row in cur:

        id = cleanRow(row[:1])

        tam = row[3:4]
        tamanho = ' '.join(tam)

        titulo = cleanRow(row[1:2])
        descr = row[1:3]
        descricao = ' '.join(descr)
        descricao = cleanText(descricao)
        descricao = ' '.join(descricao)

        line = []
        line.append(id)
        line.append(tamanho)
        line.append(descricao)

        lines.append(line)

        index = "texto/%s %s\n" % (id, tamanho)
        filename = "%s" % (id)
        txt = "%s" % (descricao)

        # #Arquivo com a tarefa
        # file = open(filename, 'w', encoding='utf8')
        # file.write(txt)

        # Arquivo único com id - tamanho
        cats.write(index)



    cur.close()
    conn.close()

    return(lines)

#"SELECT * FROM db where tamanho = 20"
#"SELECT * FROM db"
lines = importDB("SELECT * FROM db where length(descricao) + length(titulo) > 50")

textosPrincipais = open('textosPrincipais','w',encoding='utf8')
textosPrincipais.writelines(str(line)+'\n' for line in lines)
textosPrincipais.close()
# for x in lines:
#     print(x)


#------------------ createColumns -----------------#

somenteTextos = []
for line in lines:
    somenteTextos.append(line[2:])

textao = ''
for x in somenteTextos:
    textao = textao + ' ' + ' '.join(x)

textao = nltk.word_tokenize(textao)

palavras = nltk.FreqDist(w.lower() for w in textao)

maisComuns = palavras.most_common()

col = []
for x in palavras:
    col.append(x)
    # print(x)

texto = ''
for x in col:
    texto = '%s %s' % (texto, x)

t = open('colunas', 'w', encoding='utf8')
t.writelines(x+'\n' for x in col)
t.close()

t = open('attributes', 'w', encoding='utf8')
t.writelines('@ATTRIBUTE '+x+' NUMERIC\n' for x in col)
t.close()

#------------------ createMatrix  -----------------#

matrixEntrada = 'matriz02'
matrixSaida = 'matrizSaida'
matrixSaida2 = 'matrizSaida2'

#stemmer = SnowballStemmer("portuguese")

lines = somenteTextos

# textos = open(matrixEntrada, 'r', encoding='utf8')
# lines = textos.readlines()
# textos.close()

matrizA = []
matrizB = []

for line in lines:
    matI = []
    linha = ''
    line = nltk.word_tokenize(str(line)[2:len(line)-3])

    fdist = nltk.FreqDist(line)
    for i in col:

        if i in fdist:
            x = str(fdist[i])
            z = fdist[i]
            linha = linha+x.zfill(4)+' '
        else:
            z = 0
            linha = linha+'0000 '
        matI.append(z)
    linha = linha[:(len(linha)-1)]
    matrizA.append(linha)
    matrizB.append(matI)


texto = ''
for x in col:
    texto = texto+x+' '
texto = texto[:len(texto)-1]+'\n'
for m in matrizA:
    texto = texto+m+'\n'
matrix = open(matrixSaida,'w',encoding='utf8')
matrix.write(texto)
matrix.close()


texto = ''
for x in col:
    texto = texto+x+' '
texto = texto[:len(texto)-1]+'\n'
for m in matrizB:
    m = str(m)
    texto = texto+m+'\n'
matrix = open(matrixSaida2,'w',encoding='utf8')
matrix.write(texto)
matrix.close()


end = time.time()
print("\n tempo total:\n")
print('%s' % (end-start))