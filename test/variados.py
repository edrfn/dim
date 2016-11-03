# coding=utf-8

# Importação das Bibliotecas
from __future__ import print_function, unicode_literals
import nltk
from nltk.tokenize import sent_tokenize

texto = 'Este é um texto simples. Este é o pacote NLTK.'
print(sent_tokenize(texto))

texto_longo = '''
 Esta é uma demonstracao de como podemos escrever: textos
 longos. Estes\ textos longos podem ser pará/grafos inteiros
 de livros, reportagens, notícias ||e ate mesmo posts de blogs.
 Seja qual for a sua fonte, ela 'poderá' ter "textos" longos como
 este, tenha certeza disto! Força! texto
 '''

# minusculas
texto_longo = texto_longo.lower()
print(texto_longo)

# remover aspas e barra

# remover pontuação
pontos = ['.',',','!','?',';',"'",'"',':','/','|',"\\"]

for p in pontos:
    texto_longo = texto_longo.replace(p, '')


print(texto_longo)

# remover acentos
acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù',
     'ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û','ç']
s_acentos = ['a','e','i','o','u','a','e','i','o','u',
    'a','e','i','o','u','a','e','i','o','u','c']

for i in range(0, len(acentos)):
 texto_longo = texto_longo.replace(acentos[i], s_acentos[i])

print(texto_longo)

#tokenizar
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
print(word_tokenize(texto_longo))

filtrado = [w for w in word_tokenize(texto_longo) if not w in stopwords.words('portuguese')]
print(filtrado)

# remover plurais
import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("portuguese")

print(stemmer.stem("demonstrações"))

#stemmer = nltk.stem.RSLPStemmer()
filt_stem = []

for i in filtrado:
    filt_stem.append(stemmer.stem(i))

print(filt_stem)