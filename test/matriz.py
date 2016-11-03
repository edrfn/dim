# coding=utf-8
import os
import time
import glob
import nltk
import re
from unicodedata import normalize
from nltk.corpus import stopwords
path = 'ntt/'

start = time.time()


def rem_space(texto):
    ft = texto
    re.sub(r'[^\w]', ' ', ft)
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    ft = ft.replace("  ", " ")
    texto = ft
    return(texto)



#stopwords = open('stop2.txt', 'r').read().split()

textos = []
for filename in glob.glob(os.path.join(path, '*')):
    textwords = open(filename, 'r', encoding='utf8').read()

    id = str(filename[4:])
    textos.append(id + '\t' + textwords)
    for palavra in

texto = ''
for x in textos:
    texto = '%s %s \n' % (texto, x)
    texto = rem_space(texto)



t = open('matriz01', 'w')
t.write(texto)
t.close()

t2 = open('matriz01', 'r')

f2 = nltk.FreqDist(w.lower() for w in t2)
print(f2.most_common())

# x = freq_dist.keys()[:1000]
# print(x)

# def collect_all_words(self, items):
#     all_words = []
#     for item in items:
#         for w in item.all_words:
#             words.append(w)
#     return all_words
#
#
# def identify_top_words(self, all_words):
#     freq_dist = nltk.FreqDist(w.lower() for w in all_words)
#     return freq_dist.keys()[:1000]
#
# collect_all_words(glob.glob(os.path.join(path, '*'))
# #identify_top_words(all_words)

end = time.time()

print("\n tempo total:\n")
print('%s' % (end-start))