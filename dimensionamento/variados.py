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
print(sent_tokenize(texto))

texto_longo = '''Títulos Substituídos por cheques são recuperados pelo utilitário TITPED
Breve descrição do caso:



Ao rodar o TITPED em uma base que tenha sido efetuado substituição de cheques, os títulos substituídos são recuperados mesmo tendo sido substituídos por cheques.



Qual o comportamento observado?



Ao rodar o TITPED em uma base que tenha sido efetuado substituição de cheques, os títulos substituídos são recuperados mesmo tendo sido substituídos por cheques. No cadastro do cliente fica os dois títulos, o que foi substituído e o cheque.





Quais as etapas para reproduzir o comportamento observado?



> Crie um cliente novo, e uma forma de pagamento nova com vencimento para 30 dias. (Duplicata)

> Venda para esse cliente um produto e efetue o pagamento com a forma de pagamento criada (duplicata).

> Registre o recebimento e coloque o vencimento para 30 dias, logo em seguida feche o caixa.

> Efetue a SUBSTITUIÇÃO DE CHEQUES na rotina localizada no Contas a RECEBER, e substitua o titulo por um cheque com mesma data de vencimento.

> Rode o TITPED.exe na pasta AUT01.

> Entre no sistema e verifique o cadastro do cliente, na aba dos títulos (F11), verifique que somente o cheque está aparecendo.

> Efetue a reindexação do sistema.

> Verifique novamente os titulos do cliente, verifique que o titulo que foi substituído foi recuperado.



Qual o comportamento esperado?



O titulo substituído pelo cheque não deve ser recuperado na utilização do TITPED.



Quais as etapas para reproduzir o comportamento esperado?



> Crie um cliente novo, e uma forma de pagamento nova com vencimento para 30 dias. (Duplicata)

> Venda para esse cliente um produto e efetue o pagamento com a forma de pagamento criada (duplicata).

> Registre o recebimento e coloque o vencimento para 30 dias, logo em seguida feche o caixa.

> Efetue a SUBSTITUIÇÃO DE CHEQUES na rotina localizada no Contas a RECEBER, e substitua o titulo por um cheque com mesma data de vencimento.

> Rode o TITPED.exe na pasta AUT01.

> Entre no sistema e verifique o cadastro do cliente, na aba dos títulos (F11), verifique que somente o cheque está aparecendo.

> Efetue a reindexação do sistema.

> Verifique novamente os títulos do cliente.



Qual a versão do produto e sistema operacional utilizados ?



Automaster 4.5f 7268



Informações adicionais.



Esse problema não deixa que clientes que utilizam a rotina SUBSTITUIÇÃO DE CHEQUES não podem utilizar o utilitário TITPED.
 '''



# minusculas
texto_longo = texto_longo.lower()
print(texto_longo)

# remover pontuação aspas e barra

pontos = ['.', ',', '!', '?', ';', "'", '"', ':', '/', '|', "\\", '(', ')', '[', ']', '{', '}','-','#','*','@', '=', '#', '$', '%', '>','<']


# '.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','-','#','*'

for p in pontos:
    texto_longo = texto_longo.replace(p, '')

print(texto_longo)

print(sent_tokenize(texto_longo))

print(len(sent_tokenize(texto_longo)))

cab = word_tokenize(texto_longo)
filt_stem = []

for i in cab:
    filt_stem.append(stemmer.stem(i))

print(filt_stem)

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

print(word_tokenize(texto_longo))

filtrado = [w for w in word_tokenize(texto_longo) if not w in stopwords.words('portuguese')]
print('>>>>',filtrado)

# remover plurais
stemmer = SnowballStemmer("portuguese")
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
    line = line+x

print(line)
# for t in textwords:
#     filteredtext = [t.lower() for t in textwords if t.lower() not in stopwords]
