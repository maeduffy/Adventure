import MySQLdb
import re
from sys import stdin

db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

cur = db.cursor()

def addCharacter(name):
	insert = "INSERT INTO Characters VALUES (NULL, %s, 100, 1);" % name
	cur.execute(insert)
	print "Character added: "
	for row in cur.fetchall():
		print "id: " + str(row[0]) + " name: " + row[1] + " health: " + str(row[2]) + " current room: " + str(row[3])

def charExists(name):
	select = "SELECT COUNT(*) FROM (SELECT name FROM Characters WHERE name = '%') AS names;" % name
	return cur.fetchall[0][0]

def roomText(id):
	texts = 
