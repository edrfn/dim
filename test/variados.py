# coding=utf-8

# Importação das Bibliotecas
from __future__ import print_function, unicode_literals
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("portuguese")

texto = 'Este é um texto simples. Este é o pacote NLTK.'
#print(sent_tokenize(texto))

texto_longo = '''Esta é uma demonstração de como podemos escrever: textos
 longos. Estes\ textos longos podem ser pará/grafos inteiros
 de livros, reportagens, notícias ||e até mesmo posts de blogs.
 Seja qual for a sua fonte, ela 'poderá' ter "textos" longos como
 este, tenha certeza disto! Força! texto até mais, texto texto texto texto texto texto texto texto.
 '''

# minusculas
texto_longo = texto_longo.lower()
#print(texto_longo)

# remover pontuação aspas e barra

pontos = ['.',',','!','?',';',"'",'"',':','/','|',"\\"]

# '.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','-','#','*'

for p in pontos:
    texto_longo = texto_longo.replace(p, '')

#print(texto_longo)

#print(sent_tokenize(texto_longo))

#print(len(sent_tokenize(texto_longo)))

cab = word_tokenize(texto_longo)
filt_stem = []

for i in cab:
    filt_stem.append(stemmer.stem(i))

#print(filt_stem)

# # remover acentos
# acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù',
#      'ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û','ç']
# s_acentos = ['a','e','i','o','u','a','e','i','o','u',
#     'a','e','i','o','u','a','e','i','o','u','c']
#
# for i in range(0, len(acentos)):
#  texto_longo = texto_longo.replace(acentos[i], s_acentos[i])
#
# print(texto_longo)

#tokenizar

#print(word_tokenize(texto_longo))

filtrado = [w for w in word_tokenize(texto_longo) if not w in stopwords.words('portuguese')]
print(filtrado)

# remover plurais
stemmer = SnowballStemmer("portuguese")

#print(stemmer.stem("demonstrações"))

#stemmer = nltk.stem.RSLPStemmer()
filt_stem = []

for i in filtrado:
    filt_stem.append(stemmer.stem(i))

print(filt_stem)

#frequencia
fdist = nltk.FreqDist(filt_stem)

columns = []

# for i in fdist:
#     print(i + ': ' + str(fdist[i]))

for i in fdist:
    columns.append(i)

print(columns)

# matriz de palavras

col = ['rocket','escrev', 'text', 'ser', 'ter', 'demonstr', 'livr', 'forc', 'posts', 'certez', 'font', 'notíc', 'parágraf', 'long', 'blogs', 'é', 'pod', 'reportagens', 'dist', 'inteir', 'people', 'cabs']

matrizA = []
print('>>>>>',fdist)
for i in col:
    if i in fdist:
        x = str(fdist[i])

        matrizA.append(x.zfill(2))
    else:
        matrizA.append('00')

print(matrizA)

# transformar a lista acima em uma única linha da matriz
line = ''
for x in matrizA:
    line = line+' '+x

print(line)
# for t in textwords:
#     filteredtext = [t.lower() for t in textwords if t.lower() not in stopwords]

matriz02 = open('matriz02', 'r', encoding='utf8')

lines = matriz02.readlines()
for line in lines:
    print(line)
