#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:
  cur = con.cursor()
  cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s"
    ("Guy de Maupasant", "4"))

  print "Numbers of rows updated: %d" % cur.rowcount
