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

def charExists(name):
	select = "SELECT COUNT(*) FROM (SELECT name FROM Characters WHERE name = '%') AS names;" % name
	return cur.fetchall[0][0]

def roomText(id):
	texts = 
