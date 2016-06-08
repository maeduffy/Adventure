import MySQLdb
import re
from sys import stdin

db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

#db = MySQLdb.connect(host = 'localhost',
#                     user = 'root',
 #                    passwd = '123',
  #                   db = 'final')

cur = db.cursor()

def addCharacter(name):
	insert = "INSERT INTO Characters VALUES (NULL, '%s', 100, 1);" % name
	cur.execute(insert)
	db.commit()

def charExists(name):
	select = "SELECT COUNT(*) FROM (SELECT name FROM Characters WHERE name = '%s') AS names;" % name
	cur.execute(select)
	return cur.fetchall

def roomText(id):
	texts = "SELECT id, phrase FROM Rooms WHERE id = (SELECT pass1 FROM Rooms WHERE id = %d) OR id = (SELECT pass2 FROM Rooms WHERE id = %d) OR id = (SELECT pass3 FROM Rooms WHERE id = %d);" % (id, id, id)
	cur.execute(texts)
	return cur.fetchall

def addCurrentItem(char, item):
	insert = "INSERT INTO CurrentItems VALUES ('%s', %d);" % (char, item)
	cur.execute(insert)
	db.commit()

def checkProjectComplete(char, project):
	projects = "SELECT COUNT(*) FROM CompletedProjects WHERE CharId = '%s' AND id = %d;" % (char, project)
	cur.execute(projects)
	return cur.fetchall

def setProjectComplete(char, project, score):
	insert = "INSERT INTO CompletedProjects VALUES('%s', %d, %d);" % (char, project, score);
	cur.execute(insert)
	db.commit()

def checkTestComplete(char, test):
	tests = "SELECT COUNT(*) FROM CompletedProjects WHERE CharId = '%s' AND id = %d;" % (char, test)
	cur.execute(tests)
	return cur.fetchall

def setTestComplete(char, test, score):
	insert = "INSERT INTO CompletedTests VALUES('%s', %d, %d);" % (char, test, score);
	cur.execute(insert)
	db.commit()


