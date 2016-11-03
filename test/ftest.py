# coding=utf-8
import os
import time
import glob
import nltk
import re
from nltk.corpus import stopwords
path = 'ntt/'

start = time.time()
textos = []
for filename in glob.glob(os.path.join(path, '*')):
    textwords = open(filename, 'r', encoding='utf8')
    textos.append(textwords.read())

print(textos)

t = open('ftest', 'w', encoding='utf8')
t.writelines(str(x) for x in textos)
t.close()

end = time.time()

print("\n tempo total:\n")
print('%s' % (end-start))

# limpar ftest

f = open('ftest', 'r', encoding='utf8')
ft = f.read()
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
print(ft)
g = open('g', 'w', encoding='utf8')
g.write(ft)
g.close()
f.close()

