#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM Writers")

  desc = cur.description

  rows=cur.fetchall()
  print "%s %3s" % (desc[0][0], desc[1][0])

  for row in rows:
    print "%2s %3s" % row
