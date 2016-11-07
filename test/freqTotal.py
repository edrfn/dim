# coding=utf-8
import os
import time
import glob
import nltk
from nltk.corpus import stopwords
path = 'ntt/'

start = time.time()

t2 = open('matriz03', 'r', encoding='utf8').read().split()

f2 = nltk.FreqDist(w.lower() for w in t2)

f3 = f2.most_common()[:100]
t = open('top100', 'w', encoding='utf8')
t.writelines(str(x) for x in f3)
t.close()

f3 = f2.most_common()
t = open('todasFreq', 'w', encoding='utf8')
#t.writelines(str(x) for x in f3)
t.writelines(str(x) for x in f3)
t.close()

print(f2.most_common())
list = f2.most_common()
print(list)
list2 = []
for x in list:
    list2.append(x[:1])

print(list2)
texto = ''
for x in list2:
    texto = '%s %s ' % (texto, x)
    print(x)
texto = texto[1:]

texto = texto.replace('(','')
texto = texto.replace(')','')
texto = texto.replace("'",'')
texto = texto.replace(",",'')
# texto = texto.replace("\\n",'')
# texto = texto.replace("\\t",'')
# texto = texto.replace("\\s",'')


f3 = texto
t = open('colunas', 'w', encoding='utf8')
t.writelines(str(x) for x in f3)
#t.write(f3)
t.close()
