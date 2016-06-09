import MySQLdb
import re
from sys import stdin

#db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

# db = MySQLdb.connect(host = 'localhost',
#                      user = 'root',
#                     	passwd = '123',
#                    	db = 'final')

cur = db.cursor()

def addCharacter(name):
	cur.execute("INSERT INTO Characters VALUES (NULL, %s, 100, 1)", (name))
	db.commit()

def charExists(name):
	cur.execute("SELECT COUNT(*) FROM (SELECT name FROM Characters WHERE name = %s) AS names", (name))
	db.commit()
	return cur.fetchall()

def getCharRoom(id):
	pass
	# db.commit()
	# return cur.fetchall()

def roomText(id):
	cur.execute("SELECT id, phrase FROM Rooms WHERE id = (SELECT pass1 FROM Rooms WHERE id = %d) OR id = (SELECT pass2 FROM Rooms WHERE id = %d) OR id = (SELECT pass3 FROM Rooms WHERE id = %d)",
		(id, id, id))
	db.commit()
	return cur.fetchall()

def addCurrentItem(char, item):
	cur.execute("INSERT INTO CurrentItems VALUES (%s, %d)", (char, item))
	db.commit()

def checkProjectComplete(char, project):
	cur.execute("SELECT COUNT(*) FROM CompletedProjects WHERE CharId = %s AND id = %d", (char, project))
	db.commit()
	return cur.fetchall()

def setProjectComplete(char, project, score):
	cur.execute("INSERT INTO CompletedProjects VALUES(%s, %d, %d)", (char, project, score))
	db.commit()

def checkTestComplete(char, test):
	cur.execute("SELECT COUNT(*) FROM CompletedProjects WHERE CharId = %s AND id = %d", (char, test))
	db.commit()
	return cur.fetchall()

def setTestComplete(char, test, score):
	cur.execute("INSERT INTO CompletedTests VALUES(%s, %d, %d)", (char, test, score))
	db.commit()

def getRoom(charId):
	cur.execute("SELECT currentRoom FROM Characters WHERE id = %d", (charId))
	return cur.fetchall() 
