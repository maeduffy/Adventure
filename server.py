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

   def __repr__(self):
      return '<User %r>' % self.username

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
      return flask.redirect('/login?message=Error')
   
   if character == None:
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
   # render the roomId
   # add passage to the template
   # add the 3 room travel options

   if flask.request.method == 'GET':
      if user != None:
         currentRoom = int(connector.getRoom(user.userid)[0][0])
         rooms = connector.roomText(currentRoom)

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text1=rooms[0][1], 
               text2=rooms[1][1]
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text1=rooms[0][1], 
               text2=rooms[1][1], 
               text3=rooms[2][1], 
               )

   # on mouse click, get the result & reselect rooms
   if flask.request.method == 'POST':
      if user != None:
         chosenRoom = int(flask.request.form.get('form'))

         # set roomid as current room
         rooms = connector.roomText(chosenRoom)

         # add any items that the current room has to current items

         if len(rooms) < 3:
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               text1=rooms[0][1], 
               text2=rooms[1][1]
               )
         else: 
            return flask.render_template('begin.html',
               user=user.username,
               room1=rooms[0][0],
               room2=rooms[1][0],
               room3=rooms[2][0],
               text1=rooms[0][1], 
               text2=rooms[1][1], 
               text3=rooms[2][1], 
               )

   else:
      return flask.render_template('begin.html')
   
@app.route('/logout')
def logout():
   flask_login.logout_user()
   # eventually, we'll get this to a template.
   return 'Bye! You have been logged out.'

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
