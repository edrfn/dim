
# coding=utf-8
import os
import time
import glob
import nltk
from unicodedata import normalize
from nltk.corpus import stopwords
path = 'ntt/'

start = time.time()



textos = []
for filename in glob.glob(os.path.join(path, '*')):
    textwords = open(filename, 'r', encoding='utf8').read().split()
    freq_dist = nltk.FreqDist(w.lower() for w in textwords)
    textos.append(textwords)

texto = ''
for x in textos:
    texto = '%s %s ' % (texto, x)


t = open('todos', 'w', encoding='utf8')
t.write(texto)
t.close()

t2 = open('todos', 'r', encoding='utf8')

f2 = nltk.FreqDist(w.lower() for w in t2)
print(f2.most_common())
for x in f2.most_common():
    print(x[:1])

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