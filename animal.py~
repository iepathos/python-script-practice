#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as db
import sys

try:
  # Connection
  con = db.connect('localhost', 'testuser', 'test623', 'testdb')

# If connection fails find out why from database
except db.Error, e:
  print "Error %d: %s" % (e.args[0], e.args[1])
  sys.exit(1)

# Use connection
with con:
  # Cursor
  cur = con.cursor()

  # Drop table animal if it exists
  cur.execute("DROP TABLE IF EXISTS animal") 

  # Create table animal
  cur.execute("""
    CREATE TABLE animal
    (
      name  CHAR(40),
      category CHAR(40)
    )
  """)
  # Insert information into table animal
  cur.execute("""
    INSERT INTO animal(name, category)
    VALUES
      ('snake', 'reptile'),
      ('frog', 'amphibian'),
      ('tuna', 'fish'),
      ('racoon', 'mammal')
  """)

print "Number of rows inserted: %d" % cur.rowcount

# Fetch one row of information from table?
cur.execute("SELECT name, category FROM animal")
while(1):
  row = cur.fetchone()
  if row == None:
    break
  print "%s, %s" % (row[0], row[1])
print "Number of rows returned: %d" % cur.rowcount

# Practice safe-sex
cur.close()
