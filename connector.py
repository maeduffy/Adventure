import MySQLdb
import re
from sys import stdin

#db = MySQLdb.connect(host = "csc-db0", user = "cpew", passwd = "FunToPassHa7", db = "cpew")

# Michelle's local credentials. Modify if running it for yourself!
db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '123', db = 'final')

cur = db.cursor()

def addCharacter(name):
	cur.execute("""INSERT INTO Characters VALUES (NULL, %s, 100, 1)""", (name,))
	db.commit()

def charExists(name):
	cur.execute(
		"""SELECT * FROM Characters WHERE name = %s""", (name,))
	db.commit()
	return cur.fetchall()

def getRooms(userid):
	cur.execute("""SELECT id FROM Rooms WHERE id = (SELECT pass1 FROM Rooms WHERE id = '%s') OR id = (SELECT pass2 FROM Rooms WHERE id = '%s') OR id = (SELECT pass3 FROM Rooms WHERE id = '%s')""",
		(userid, userid, userid))
	db.commit()
	return cur.fetchall()

def roomText(roomId):
	cur.execute("""SELECT phrase FROM Rooms WHERE id = %s""", (roomId,))
	db.commit()
	return cur.fetchall()

def addCurrentItem(char, item):
	cur.execute("""INSERT INTO CurrentItems VALUES ('%s', %s)""", (char, item))
	db.commit()

def checkProjectComplete(char, project):
	cur.execute("""SELECT COUNT(*) FROM CompletedProjects WHERE CharId = '%s' AND id = %s""", (char, project))
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
	cur.execute("""UPDATE Characters SET currentRoom = %s WHERE id = %s""", (roomId, charId))
	db.commit()

def getItemIdFromRoom(roomID):
	cur.execute("""SELECT itemID FROM Rooms WHERE id = %s""", (roomID,))
	db.commit()
	return cur.fetchall()

def getProjectFromRoom(roomID):
	cur.execute("""SELECT projectID FROM Rooms WHERE id = %s""", (roomID,))
	db.commit()
	return cur.fetchall()

def getTestName(testID):
	cur.execute("""SELECT name FROM Tests WHERE id = %s""", (testID,))
	return cur.fetchall()

def getQuestion(testID, questionID):
	cur.execute("""SELECT question FROM Questions WHERE test = %s AND testQuestion = %s""", (testID, questionID))
	return cur.fetchall()

def getAnswer(testID, questionID):
	cur.execute("""SELECT answer FROM Questions WHERE test = %s AND testQuestion = %s""", (testID, questionID))
	return cur.fetchall()

#Please pass in negative number if health is decreasing
def changeHealth(percentChange, charID):
	cur.execute("""UPDATE Characters SET health = health + %s WHERE id = %s""", (percentChange, charID))
	db.commit()

def healthMeaning(health):
	cur.execute("""SELECT meaning FROM Health WHERE percent = %s""", (health,))
	return cur.fetchall()

def getItemDesc(itemId):
	cur.execute("""SELECT message FROM Items WHERE id = %s""", (itemId,))
	db.commit()
	return cur.fetchall()

def nextTest(charId):
	cur.execute("""SELECT COUNT(*) FROM CompletedTests WHERE charID = %d""", (charId))
	completeCount = cur.fetchall()[0][0]
	cur.execute("""SELECT COUNT(*) FROM Tests""")
	testCount = cur.fetchall()[0][0]
	if (completeCount == testCount):
		return False
	else:
		return testCount - (testCount - completeCount) + 1

def projectItems(projectId):
	cur.execute("""SELECT itemID FROM ProjectItems WHERE projectID = %s""", (projectId))
	return cur.fetchall()

# check existence in currentItems, return true/false
def checkObtainedItemExists(itemId):
	cur.execute("""SELECT COUNT(*) FROM CurrentItems WHERE id = %d""", (itemId))
	if (cur.fetchall()[0][0] == 0):
		return False
	else:
		return True

# check existence in Items for use in Project, return true/false
def checkCurrentItemExists(itemId):
	
	return False
	return True

def getProjectMessage(projectId):
	cur.execute("""SELECT message FROM Projects WHERE projectID = %d""", (projectId))
	return cur.fetchall()
