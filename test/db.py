#!/usr/bin/env python
#from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='bitnami_redmine')

cur = conn.cursor()

#cur.execute("SELECT * FROM db where tamanho = 20")
cur.execute("SELECT * FROM db")

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

    file = open(filename, 'w', encoding='utf8')
    file.write(txt)

    cats.write(index)

print(cur.rowcount)


cur.close()
conn.close()