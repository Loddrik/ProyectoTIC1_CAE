from flask import Flask,render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_bootstrap import Bootstrap


def create_app():
   app = Flask(__name__)
   Bootstrap(app)

   return app


app = create_app()
#Ruta de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///nuevabd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Inicializar base de datos
db = SQLAlchemy(app)

#create db model
class Users(db.Model):
   id = db.Column('user_id',db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   nickname = db.Column(db.String(10))
   passw = db.Column(db.String(20))

   def __init__(self, name,nickname,passw):
      self.name = name
      self.nickname = nickname
      self.passw = passw



@app.route('/register', methods=['GET', 'POST'])
def reg():
   if request.method== 'POST':
      if not request.form['name'] or not request.form['passw'] or not request.form['nickname']:
         return rediret('/register')
      #Login
      else:
         user = Users(request.form['name'],request.form['nickname'],request.form['passw'])
         db.session.add(user)
         db.session.commit()
         #flash('Guardado correctamente')
         return redirect('/register')

   else:
      #Register
      usuarios = Users.query.all()

      return render_template('login.html',usuarios = usuarios)


@app.route('/appcae')
def APPCAE():
  #si existen simulaciones:
   return render_template('app.html')
  #si no:
   #return  render template()



@app.route('/redes', methods=['GET', 'POST'])
def redes():
   return render_template('redes.html')

@app.route('/')
def home():
   return render_template('inicio.html')
   pass

if __name__ == "__main__":
	app.run(debug=True)