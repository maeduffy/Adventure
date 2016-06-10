import flask
import flask_login
import logging
import os
import MySQLdb
import connector

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
         currentRoom = int(connector.getRoom(user.userid)[0][0])
         rooms = connector.getRooms(currentRoom)
         text = connector.roomText(currentRoom)[0][0]

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text=text,
               room=currentRoom
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text=text,
               room=currentRoom
               )

   # on mouse click, get the result & reselect rooms
   if flask.request.method == 'POST':
      if user != None:
         currentRoom = int(flask.request.form.get('form'))
         rooms = connector.getRooms(currentRoom)
         text = connector.roomText(currentRoom)[0][0]
        
         itemId = connector.getItemIdFromRoom(currentRoom)[0][0]

         if itemId != None:
            item = connector.getItemDesc(itemId)[0][0]
            # need connector here to confirm whether itemId already exists for user
            connector.addCurrentItem(user.userid, itemId)

            if len(rooms) < 3:
               return flask.render_template('begin.html',
                  user=user.username,
                  room1=rooms[0][0],
                  room2=rooms[1][0],
                  text=text,
                  room=currentRoom,
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
                  item=item
                  )

         projectId = connector.getProjectFromRoom(currentRoom)[0][0]
         if projectId != None and connector.checkProjectComplete(user.userid, projectId)[0][0] != None:
            projectItems = connector.projectItems(projectId)

            allItemsExist = True
            for pItem in projectItems:
               pItem = pItem[0]
               if connector.checkCurrentItemExists(pItem) == False:
                  allItemsExist = False
                  break

            if allItemsExist:
               connector.setProjectComplete(char, project, randint(0, 100))
               message = connector.getProjectMessage(projectId)[0][0]

               if len(rooms) < 3:
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     text=text,
                     room=currentRoom,
                     project=message
                     )
               else: 
                  return flask.render_template('begin.html',
                     user=user.username,
                     room1=rooms[0][0],
                     room2=rooms[1][0],
                     room3=rooms[2][0],
                     text=text,
                     room=currentRoom,
                     project=message
                     )

         # generate random test
         else:
            status = connector.nextTest()
            # all tests are completed if status is False
            # if status != False:
               # rand = random.randint(0, 10)
               # if rand == 10:

               # I guess we'd probably load some new HTML page to represent a test

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text=text,
               room=currentRoom
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text=text,
               room=currentRoom
               )

   else:
      print "This should never happen, ideally."
      return flask.render_template('begin.html')
   
@app.route('/logout')
def logout():
   flask_login.logout_user()
   return flask.render_template('logout.html')

@login_manager.unauthorized_handler
def unauthorized_handler():
   return 'Unauthorized to access.'

@login_manager.user_loader
def user_loader(userid):
   # identify the user by their Character id
   return user

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
