import flask
import flask_login
import logging
import os
import MySQLdb
import connector

user = None
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

class User():
   def __init__(self, username, id):
      self.username = username
      self.id = id

   def is_authenticated(self):
      if self.id != None:
         return True
      else:
         return False

   def is_active(self):
      return True

   def is_anonymous(self):
      return True

   def get_id(self):
      return self.id

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
         
      return flask.redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
   if flask.request.method == 'GET':
      return flask.render_template('login.html',
         message=flask.request.args.get('message'))
   
   # else, if they are already trying to log in
   username = flask.request.form['name']
   
   try:
      # Get a connector python method that checks for Character existence.
      statement = "SELECT * FROM Characters WHERE name = '%s'" % username
      cur.execute(statement)
      db.commit()
      character = cur.fetchall()
      # print "Received", character
   except MySQLdb.Error as e:
         return flask.redirect('/login?message=Error')
   
   if character == None:
      return flask.redirect('/login?message=Error')

   user = User(character[0][1], character[0][0])
   print user

   flask_login.login_user(user)
   return flask.redirect(flask.url_for('index'))

@app.route('/', methods=['GET'])
def index():
   if user != None and user.is_authenticated:
      print user, user.username, flask_login.current_user.username
      return flask.render_template('index.html', user=user.username)

   else:
      print user
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

# @app.route('/protected', methods=['GET', 'POST']) 
# @flask_login.login_required
# def protected():
#   return "Logged in as: " + flask_login.current_user.username

@login_manager.user_loader
def user_loader(userid):
   # identify the user by their Character id
   if user != None:
      return user.get(user.id)
   else:
      return None

@login_manager.request_loader
def request_loader(request):
   # first, try to login using the api_key url arg
   api_key = request.args.get('api_key')
   if api_key:
      user = User.query.filter_by(api_key=api_key).first()
      if user:
         return user

   return None

if __name__ == "__main__":
   app.run(debug=True, port=8000)
