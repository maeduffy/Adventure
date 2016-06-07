import flask
import flask_login
import logging
import os
import MySQLdb

app = flask.Flask(__name__)
app.secret_key = os.urandom(16).encode('hex')
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

logging.basicConfig(level=logging.DEBUG)
db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = '123',
                     db = 'final')
cur = db.cursor()

class User(flask_login.UserMixin):
   pass


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   if flask.request.method == 'GET':
      return flask.render_template('signup.html',
         message=flask.request.args.get('message'))
   
   if flask.request.method == 'POST':
      name = flask.request.form.get('name')
      try:
         # replace with connector method once done.
         data = (name)
         cur.execute("INSERT INTO Characters "
          "(id, name, health, currentRoom) VALUES (1, '%s', 0, 0)", data) 

      except MySQLdb.Error as e:
         return flask.redirect('/signup?message=Error.')
         
      return flask.redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
   if flask.request.method == 'GET':
      return flask.render_template('login.html')
   
   # else, if they are already trying to log in
   username = flask.request.form['username']
   user = User()
   # Get a connector python method that checks for Character existence.
   cur.execute("SELECT * FROM Characters WHERE name = ?", (name))
   character = cur.fetchone()
   
   if character == None:
      return "Bad login"

   user.id = character[0]
   user.username = character[1]
   flask_login.login_user(user)

   return flask.redirect(flask.url_for('/'))

@app.route('/', methods=['GET'])
def index():
   return flask.render_template('index.html')
      
@app.route('/begin')
@flask_login.login_required
def begin():
   pass
   
@app.route('/logout')
def logout():
   flask_login.logout_user()
   return 'Bye! You have been logged out.'

@login_manager.unauthorized_handler
def unauthorized_handler():
   return 'Unauthorized to access.'

#@app.route('/protected', methods=['GET', 'POST']) 
#@flask_login.login_required
#def protected():
#   return "Logged in as: " + flask_login.current_user.username

"""
@login_manager.user_loader
def user_loader(user):
   cur.execute("SELECT id FROM Characters WHERE name = ?", (name))
   character = cur.fetchone()
   if character == None:
      return
   user = User()
   user.id = character[0]

   # identify the user by their Character id
   return user

@login_manager.request_loader
def request_loader(request):
   username = request.form.get('name')
   cur.execute("SELECT * FROM Characters WHERE name = ?", (username))
   character = cur.fetchone()
   if character == None:
      return

   user = User()
   user.id = character[0]

   # just pretend authentication was defaulted, as long as they existed
   return user
"""

if __name__ == "__main__":
   app.run(debug=True, port=8000)
