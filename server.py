import flask
import flask_login
import logging
import os
import MySQLdb
import connector
import random

from flask_bootstrap import Bootstrap

user = None
app = flask.Flask(__name__)
Bootstrap(app)
app.secret_key = os.urandom(16).encode('hex')
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

logging.basicConfig(level=logging.DEBUG)

class User(flask_login.UserMixin):
   def __init__(self, username, userid):
      self.username = username
      self.userid = userid
      self.testId = None

   def is_authenticated(self):
      return True

   def is_active(self):
      return True

   def is_anonymous(self):
      return True

   def get_id(self):
      return chr(self.userid)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   if flask.request.method == 'GET':
      return flask.render_template('signup.html',
         message=flask.request.args.get('message'))
   
   if flask.request.method == 'POST':
      name = flask.request.form.get('name')
      try:
         connector.addCharacter(name)

      except MySQLdb.Error as e:
         print e
         return flask.redirect('/signup?message=Error')
         
      return flask.redirect(flask.url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
   global user

   if flask.request.method == 'GET':
      return flask.render_template('login.html',
         message=flask.request.args.get('message'))
   
   # else, if they are already trying to log in
   username = flask.request.form['name']
   
   try:
      character = connector.charExists(username)
   except MySQLdb.Error as e:
      print e
      return flask.redirect('/login?message=Error')
   
   if not character:
      return flask.redirect('/login?message=Error')

   user = User(username, int(character[0][0]))
   flask_login.login_user(user, remember=True)

   return flask.redirect(flask.url_for('index'))

@app.route('/', methods=['GET'])
def index():
   if user != None and user.is_authenticated():
      return flask.render_template('index.html', user=user.username)
   else:
      return flask.render_template('index.html')
      
@app.route('/begin', methods=['GET', 'POST'])
@flask_login.login_required
def begin():
   if flask.request.method == 'GET':
      if user != None:
         health = connector.getHealth(user.userid)[0][0]
         currentRoom = int(connector.getRoom(user.userid)[0][0])
         rooms = connector.getRooms(currentRoom)
         text = connector.roomText(currentRoom)[0][0]

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text=text,
               room=currentRoom,
               health=health
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text=text,
               room=currentRoom,
               health=health
               )

   # on mouse click, get the result & reselect rooms
   if flask.request.method == 'POST':
      if user != None:
         health = connector.getHealth(user.userid)[0][0]

         currentRoom = flask.request.form.get('form')
         if currentRoom != None:
            currentRoom = int(currentRoom)
         else:
            currentRoom = int(connector.getRoom(user.userid)[0][0])

         connector.setRoom(user.userid, currentRoom)
         rooms = connector.getRooms(currentRoom)
         text = connector.roomText(currentRoom)[0][0]

         if checkGameComplete() != False:
            text = checkGameComplete()
            return flask.render_template('begin.html',
               user=user.username,
               text=text,
               room=currentRoom,
               health=health
               )
        
         if user.testId != None:
            currentRoom = int(connector.getRoom(user.userid)[0][0])
            answer1 = flask.request.form.get('f1')
            answer2 = flask.request.form.get('f2')
            answer3 = flask.request.form.get('f3')
            answer4 = flask.request.form.get('f4')
            answer5 = flask.request.form.get('f5')

            correctAnswer1 = connector.getAnswer(user.testId, 1)[0][0]
            correctAnswer2 = connector.getAnswer(user.testId, 2)[0][0]
            correctAnswer3 = connector.getAnswer(user.testId, 3)[0][0]
            correctAnswer4 = connector.getAnswer(user.testId, 4)[0][0]
            correctAnswer5 = connector.getAnswer(user.testId, 5)[0][0]

            studentAnswers = (answer1, answer2, answer3, answer4, answer5)
            testAnswers = (correctAnswer1, correctAnswer2, correctAnswer3,
               correctAnswer4, correctAnswer5)
            score = compareAnswers(studentAnswers, testAnswers)

            # Mark test as completed.
            connector.setTestComplete(user.userid, user.testId, score)
            user.testId = None
            affectedHealth = connector.getHealthFromScore(score)[0][0]
            connector.changeHealth(affectedHealth, user.userid)

            if len(rooms) < 3:
               return flask.render_template('begin.html',
                  user=user.username,
                  room1=rooms[0][0],
                  room2=rooms[1][0],
                  text=text,
                  room=currentRoom,
                  health=health,
                  a1=answer1,
                  a2=answer2,
                  a3=answer3,
                  a4=answer4,
                  a5=answer5,
                  score=score
                  )
            else:
               return flask.render_template('begin.html',
                  user=user.username,
                  room1=rooms[0][0],
                  room2=rooms[1][0],
                  room3=rooms[2][0],
                  text=text,
                  room=currentRoom,
                  health=health,
                  a1=answer1,
                  a2=answer2,
                  a3=answer3,
                  a4=answer4,
                  a5=answer5,
                  score=score
                  )

         itemId = connector.getItemIdFromRoom(currentRoom)[0][0]

         if itemId != None:
            if connector.checkObtainedItemExists(user.userid, itemId) == False:
               connector.addCurrentItem(user.userid, itemId)

               item = connector.getItemDesc(itemId)[0][0]

               if len(rooms) < 3:
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     text=text,
                     room=currentRoom,
                     health=health,
                     item=item
                     )
               else:
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     room3=rooms[2][0],
                     text=text,
                     room=currentRoom,
                     health=health,
                     item=item
                     )

         projectId = connector.getProjectFromRoom(currentRoom)[0][0]
         if projectId != None and connector.checkProjectComplete(user.userid, projectId)[0][0] != None:
            projectItems = connector.projectItems(projectId)

            allItemsExist = True
            for pItem in projectItems:
               pItem = pItem[0]
               if connector.checkObtainedItemExists(user.userid, pItem) == False:
                  allItemsExist = False
                  break

            if allItemsExist:
               score = randint(0, 10) * 10
               connector.setProjectComplete(user.userid, projectId, score)
               message = connector.getProjectMessage(projectId)[0][0]

               affectedHealth = connector.getHealthFromScore(score)[0][0]
               connector.changeHealth(affectedHealth, user.userid)

               if len(rooms) < 3:
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     text=text,
                     room=currentRoom,
                     health=health,
                     project=message,
                     score=score
                     )
               else: 
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     room3=rooms[2][0],
                     text=text,
                     room=currentRoom,
                     health=health,
                     project=message,
                     score=score
                     )

         else:
            testId = connector.nextTest(user.userid)

            # all tests are completed if testId is False
            if testId != False:
               rand = random.randint(1, 10)
               if rand == 10:
                  user.testId = testId
                  test = connector.getTestName(testId)[0][0]

                  question1 = connector.getQuestion(testId, 1)[0][0]
                  question2 = connector.getQuestion(testId, 2)[0][0]
                  question3 = connector.getQuestion(testId, 3)[0][0]
                  question4 = connector.getQuestion(testId, 4)[0][0]
                  question5 = connector.getQuestion(testId, 5)[0][0]

                  if len(rooms) < 3:
                     return flask.render_template('begin.html',
                        user=user.username,
                        room1=rooms[0][0],
                        room2=rooms[1][0],
                        text=text,
                        room=currentRoom,
                        health=health,
                        test=test,
                        q1=question1,
                        q2=question2,
                        q3=question3,
                        q4=question4,
                        q5=question5
                        )
                  else: 
                     return flask.render_template('begin.html',
                        user=user.username,
                        room1=rooms[0][0],
                        room2=rooms[1][0],
                        room3=rooms[2][0],
                        text=text,
                        room=currentRoom,
                        health=health,
                        test=test,
                        q1=question1,
                        q2=question2,
                        q3=question3,
                        q4=question4,
                        q5=question5
                        )

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text=text,
               room=currentRoom,
               health=health
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text=text,
               room=currentRoom,
               health=health
               )

   else:
      print "This should never happen, ideally."
      return flask.render_template('begin.html')
   
@app.route('/logout')
def logout():
   flask_login.logout_user()
   return flask.render_template('logout.html')

@app.route('/leaderboard')
def leaderboard():
   # load all Characters, health
   connector

   return flask.render_template('leaderboard.html')

@login_manager.unauthorized_handler
def unauthorized_handler():
   return 'Unauthorized to access.'

@login_manager.user_loader
def user_loader(userid):
   # identify the user by their Character id
   return user

def compareAnswers(studentAnswers, testAnswers):
   score = 0

   for i in range(len(studentAnswers)):
      # print studentAnswers[i], testAnswers[i]
      if studentAnswers[i] == testAnswers[i]:
         score += 20

   return score

def checkGameComplete():
   health = connector.getHealth(user.userid)
   if health == 0:
      return "You died! Game over."
   elif connector.nextTest(user.userid) == False and \
      connector.nextProject(user.userid) == False:
      return "You've finished the game! You passed CPE 357! Onwards to the next class..."
   else:
      return False

@login_manager.request_loader
def request_loader(request):
   # first, try to login using the api_key url arg

   # print '\n', 'HOW DID WE GET HERE.', '\n'
   # api_key = request.args.get('api_key')
   # if api_key:
   #    user = User.query.filter_by(api_key=api_key).first()
   #    if user:
   #       return user

   return None

if __name__ == "__main__":
   app.run(debug=True, port=8000)
