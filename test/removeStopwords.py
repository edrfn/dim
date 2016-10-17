import os
import glob
import time
import nltk
from nltk.corpus import stopwords
path = 'tt/'

start = time.time()

stopwords = open('stop2.txt', 'r').read().split()
stopwords.append(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','-','#','*',])

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
    texto = texto.replace(".", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace("*", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace("-", " ")
    texto = texto.replace("#", " ")
    texto = texto.replace("=", " ")
    texto = texto.replace("@", " ")
    texto = texto.replace('"', " ")
    texto = texto.replace('[', " ")
    texto = texto.replace(']', " ")
    texto = texto.replace('(', " ")
    texto = texto.replace(')', " ")
    texto = texto.replace('/', " ")
    texto = texto.replace(">", " ")
    texto = texto.replace("|", " ")
    t2.write(texto)

    # fim = time.time()
    # print("\n tempo montando texto:\n")
    # print(fim-ini)

end = time.time()

print("\n tempo total:\n")
print(end-start)





