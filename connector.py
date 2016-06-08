import MySQLdb
import re
from sys import stdin

# db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = '123',
                     db = 'final')

cur = db.cursor()

def addCharacter(name):
   insert = "INSERT INTO Characters VALUES (NULL, '%s', 100, 1)" % name
   cur.execute(insert)
   db.commit()

   # print "Character added: "
   # for row in cur.fetchall():
   #    print "id: " + str(row[0]) + " name: " + row[1] + " health: " + str(row[2]) + " current room: " + str(row[3])