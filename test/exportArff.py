# coding=utf-8

# Importação das Bibliotecas
from __future__ import print_function, unicode_literals
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import scipy

attributes = 'matrizSaida'
matrixNum = 'matriz02'

def generateArff(file):
    data = open(file,'r')



texto_longo = open(matrixEntrada, 'r', encoding='utf8')

lines = texto_longo.readlines()

texto_longo.close()
#print(sent_tokenize(texto_longo))

#print(len(sent_tokenize(texto_longo)))

#lines.replace('\\n','.')
#print(lines)
textinho = ''

for linha in lines:
    #linha.replace('\n','.')

    textinho = textinho+' '+linha

#print(textinho)

palavras = word_tokenize(textinho)

#frequencia
fdist = nltk.FreqDist(palavras)

col = []

for i in fdist:
    col.append(i)

textos = open(matrixEntrada, 'r', encoding='utf8')
lines = textos.readlines()
textos.close()

matrizA = []
matrizB = []

for line in lines:
    matI = []
    #print('111',line)
    line = word_tokenize(line)
    #print('222',line)
    linha = ''

    fdist = nltk.FreqDist(line)
    for i in col:
        if i in fdist:
            x = str(fdist[i])
            z = fdist[i]
            linha = linha+x.zfill(2)+' '
        else:
            z = 0
            linha = linha+'00 '
        matI.append(z)
    linha = linha[:(len(linha)-1)]
    matrizA.append(linha)
    matrizB.append(matI)


texto = ''
for m in matrizA:
    print(m)
    texto = texto+m+'\n'

print(len(matrizA))
print(matrizA)
print(matrizB)

file = open(matrixSaida,'w',encoding='utf8')

file.write(texto)

file.close()



