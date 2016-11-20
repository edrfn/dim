# coding=utf-8
import os
import time
import glob
import nltk
from nltk.corpus import stopwords
path = 'ntt/'


matrixEntrada = 'matriz02'
saida = 'colunas02'
top100saida = 'top100'
todosSaida = 'allFreq'


start = time.time()

t2 = open(matrixEntrada, 'r', encoding='utf8').read().split()

f2 = nltk.FreqDist(w.lower() for w in t2)

f3 = f2.most_common()[:100]
t = open(top100saida, 'w', encoding='utf8')
t.writelines(str(x) for x in f3)
t.close()

f3 = f2.most_common()
t = open(todosSaida, 'w', encoding='utf8')
#t.writelines(str(x) for x in f3)
t.writelines(str(x) for x in f3)
t.close()

#print(f2.most_common())
list = f2.most_common()
#print(list)
list2 = []
for x in list:
    list2.append(x[:1])

#print(list2)
texto = ''
for x in list2:
    texto = '%s %s' % (texto, x)
    #print(x)
texto = texto[1:]

texto = texto.replace('(','')
texto = texto.replace(')','')
texto = texto.replace("'",'')
texto = texto.replace(",",'')
# texto = texto.replace("\\n",'')
# texto = texto.replace("\\t",'')
# texto = texto.replace("\\s",'')

f3 = texto
print(f3)
t = open(saida, 'w', encoding='utf8')
t.writelines(str(x) for x in f3)
#t.write(f3)
t.close()
