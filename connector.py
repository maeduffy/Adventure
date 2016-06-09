import MySQLdb
import re
from sys import stdin

#db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                    	passwd = '123',
                   	db = 'final')

cur = db.cursor()

def addCharacter(name):
	cur.execute("""INSERT INTO Characters VALUES (NULL, '%s', 100, 1)""", (name,))
	db.commit()

def charExists(name):
	cur.execute(
		"""SELECT * FROM Characters WHERE name = %s""", (name,))
	db.commit()
	return cur.fetchall()

def roomText(userid):
	cur.execute("""SELECT id, phrase FROM Rooms WHERE id = (SELECT pass1 FROM Rooms WHERE id = '%s') OR id = (SELECT pass2 FROM Rooms WHERE id = '%s') OR id = (SELECT pass3 FROM Rooms WHERE id = '%s')""",
		(userid, userid, userid))
	db.commit()
	return cur.fetchall()

def addCurrentItem(char, item):
	cur.execute("""INSERT INTO CurrentItems VALUES ('%s', %s)""", (char, item))
	db.commit()

def checkProjectComplete(char, project):
	cur.execute("""SELECT COUNT(*) FROM CompletedProjects WHERE CharId = '%s' AND id = %d""", (char, project))
	db.commit()
	return cur.fetchall()

def setProjectComplete(char, project, score):
	cur.execute("""INSERT INTO CompletedProjects VALUES('%s', %s, %s)""", (char, project, score))
	db.commit()

def checkTestComplete(char, test):
	cur.execute("""SELECT COUNT(*) FROM CompletedProjects WHERE CharId = '%s' AND id = %s""", (char, test))
	db.commit()
	return cur.fetchall()

def setTestComplete(char, test, score):
	cur.execute("""INSERT INTO CompletedTests VALUES('%s', %s, %s)""", (char, test, score))
	db.commit()

def getRoom(charId):
	cur.execute("""SELECT currentRoom FROM Characters WHERE id = %s""", (charId,))
	db.commit()
	return cur.fetchall() 

def setRoom(charId, roomId):
	cur.execute("""UPDATE Characters SET currentRoom = %d WHERE id = %d""", (roomId, charId))
	db.commit()

def getItemIdFromRoom(roomID):
	cur.execute("""SELECT itemID FROM Rooms WHERE id = %d""", (roomID))
	db.commit()

def getProjectFromRoom(roomID):
	cur.execute("""SELECT projectID FROM Rooms WHERE id = %d""", (roomID))
	db.commit()

def getTestName(testID):
	cur.execute("""SELECT name FROM Tests WHERE id = %d""", (testID))
	return cur.fetchall()

def getQuestion(testID, questionID):
	cur.execute("""SELECT question FROM Questions WHERE test = %d AND testQuestion = %d""", (testID, questionID))
	return cur.fetchall()

def getAnswer(testID, questionID):
	cur.execute("""SELECT answer FROM Questions WHERE test = %d AND testQuestion = %d""", (testID, questionID))
	return cur.fetchall()

#Please pass in negative number if health is decreasing
def changeHealth(percentChange, charID):
	cur.execute("""UPDATE Characters SET health = health + %d WHERE id = %d""", (percentChange, charID))
	db.commit()

def healthMeaning(health):
	cur.execute("""SELECT meaning FROM Health WHERE percent = %d""", (health))
	return cur.fetchall()
