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
class Sim(db.Model):
   
   id = db.Column('algo_id',db.Integer, primary_key = True)

   nombre = db.Column(db.String(100))
   monto = db.Column(db.Integer())
   interes = db.Column(db.Float())
   meses = db.Column(db.Integer())
   gastos_asociados = db.Column(db.Integer)
   seguro_desgravamen = db.Column(db.Integer())
   seguros_extra = db.Column(db.Integer())
   tir = db.Column(db.Float())
   cae = db.Column(db.Float())
   interes_total = db.Column(db.Float())
   monto_bruto = db.Column(db.Float())
   monto_final = db.Column(db.Float())
   





   
   passw = db.Column(db.String(20))

   def __init__(self, nombre,monto,interes,meses,gastos_asociados,seguro_desgravamen,seguros_extra,tir,cae,interes_total,monto_bruto,monto_final):
      self.nombre = nombre
      self.monto = monto
      self.interes = interes
      self.meses = meses
      self.gastos_asociados = gastos_asociados
      self.seguro_desgravamen = seguro_desgravamen
      self.seguros_extra = seguros_extra
      self.tir = tir
      self.cae = cae
      self.interes_total = interes_total
      self.monto_bruto = monto_bruto
      self.monto_final = monto_final





@app.route('/app', methods=['GET', 'POST'])
def sim():
   if request.method== 'POST':
      
      sim = Sim(request.form['name'],request.form['nickname'],request.form['passw'])
      db.session.add(user)
      db.session.commit()
      #flash('Guardado correctamente')
      return redirect('/app')

   else:
      #Register
      simulaciones = Sim.query.all()

      return render_template('login.html',simulaciones = simulaciones)


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