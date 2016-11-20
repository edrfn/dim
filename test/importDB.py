#!/usr/bin/env python
# coding=utf-8

# - - - Extração dos dados do banco de dados e criação de vários arquivos de nome Id da tarefa, contendo o título e texto da tarefa
# - - - Criação de arquivo único de índice, contendo o id da tarefa e o tamanho da mesma

from __future__ import print_function
import pymysql

# Conexão com o banco de dados
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='bitnami_redmine')

# cursor de operações
cur = conn.cursor()

# Teste para selecionar apenas tarefas de um determinado tamanho
#cur.execute("SELECT * FROM db where tamanho = 20")

# Select
cur.execute("SELECT id, tamanho, titulo, descricao FROM db")

print(cur.description)

cats = open("cats.txt", "a", encoding='utf8')

for row in cur:

    id = row[:1]
    tamanho = row[3:4]
    titulo = "%s" % row[1:2]
    descricao = "%s" % (row[2:3])

    index = "texto/%s %s\n" % (id, tamanho)
    filename = "%s" % (id)
    txt = "%s\n%s" % (titulo, descricao)

    # Arquivo com a tarefa
    file = open(filename, 'w', encoding='utf8')
    file.write(txt)

    # Arquivo único com id - tamanho
    cats.write(index)

print(cur.rowcount)

cur.close()
conn.close()