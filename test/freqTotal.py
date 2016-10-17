import os
import time
import glob
import nltk
from nltk.corpus import stopwords
path = 'ntt/'

start = time.time()

t2 = open('g', 'r').read().split()

f2 = nltk.FreqDist(w.lower() for w in t2)

f3 = f2.most_common()[:100]
t = open('top100', 'w')
t.writelines(str(x) for x in f3)
t.close()

f3 = f2.most_common()
t = open('todasFreq', 'w')
t.writelines(str(x) for x in f3)
t.close()