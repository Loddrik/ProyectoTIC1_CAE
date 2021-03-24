from flask import Flask,render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_bootstrap import Bootstrap
from algoritmo import Algoritmo

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
   cuota = db.Column(db.Integer())
   tir = db.Column(db.Float())
   cae = db.Column(db.Float())
   interes_total = db.Column(db.Integer())
   monto_bruto = db.Column(db.Integer())
   monto_final = db.Column(db.Integer())
   

   def __init__(self, nombre,monto,interes,meses,gastos_asociados,seguro_desgravamen,seguros_extra,cuota,tir,cae,interes_total,monto_bruto,monto_final):
      self.nombre = nombre
      self.monto = monto
      self.interes = interes
      self.meses = meses
      self.gastos_asociados = gastos_asociados
      self.seguro_desgravamen = seguro_desgravamen
      self.seguros_extra = seguros_extra
      # HAsta aqui se pide en el formulario
      self.cuota = cuota
      self.tir = tir
      self.cae = cae
      self.interes_total = interes_total
      self.monto_bruto = monto_bruto
      self.monto_final = monto_final




@app.route('/simulador', methods=['GET', 'POST'])
def sim():

   if request.method == 'POST':
      nombre = str(request.form['creditname'])
      capital = int(request.form['creditamount'])
      interes = float(request.form['creditinterest'])
      meses = int(request.form['creditterm'])
      gastos_asociados = int(request.form['creditexpense'])
      if request.form['creditinsurance']:
         seguro_desgravamen = int(request.form['creditinsurance'])
      else:
         seguro_desgravamen = int(0)
      if request.form['creditinsuranceextra']:
         seguros_extra = int(request.form['creditinsuranceextra'])
      else:
         seguros_extra = int(0)
      
      tir,cae,interes_total,monto_bruto, monto_final,cuota= Algoritmo(capital,interes,
      meses,gastos_asociados,seguro_desgravamen+seguros_extra)

      sim = Sim(nombre,capital,interes,meses,gastos_asociados,seguro_desgravamen,seguros_extra,int(cuota),tir,cae,int(interes_total),int(monto_bruto),int(monto_final))
      db.session.add(sim)
      #db.session.query.order_by(Sim.monto_final.desc())

      db.session.commit()

      # flash('Guardado correctamente')
      return redirect('/simulador')

   else:
      #Register/
      simulaciones = Sim.query.all()
      

      return render_template('simulador.html',simulaciones = simulaciones)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
      task_to_delete = Sim.query.get_or_404(id)
      try:
         db.session.delete(task_to_delete) 
         db.session.commit()
         return redirect('/simulador')
      except:
         return 'Hubo un problema, no se pudo eliminar la simulacion'
         
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
   credit_to_edit = Sim.query.get_or_404(id)
   if request.method == 'POST':
      credit_to_edit.nombre = str(request.form['creditname'])
      credit_to_edit.monto = int(request.form['creditamount'])
      credit_to_edit.interes = float(request.form['creditinterest'])
      credit_to_edit.meses = int(request.form['creditterm'])
      credit_to_edit.gastos_asociados = int(request.form['creditexpense'])
      if request.form['creditinsurance']:
         credit_to_edit.seguro_desgravamen = int(request.form['creditinsurance'])
      else:
         credit_to_edit.seguro_desgravamen = int(0)
      if request.form['creditinsuranceextra']:
         credit_to_edit.seguros_extra = int(request.form['creditinsuranceextra'])
      else:
         credit_to_edit.seguros_extra = int(0)
      
      tir,cae,interes_total,monto_bruto, monto_final,cuota= Algoritmo(credit_to_edit.monto, credit_to_edit.interes,
      credit_to_edit.meses, credit_to_edit.gastos_asociados, credit_to_edit.seguro_desgravamen + credit_to_edit.seguros_extra)

      credit_to_edit.cuota = int(cuota)
      credit_to_edit.tir = tir
      credit_to_edit.cae = cae
      credit_to_edit.interes_total = int(interes_total)
      credit_to_edit.monto_bruto = int(monto_bruto)
      credit_to_edit.monto_final = int(monto_final)

      try:
         db.session.commit()
         return redirect('/simulador')
      except:
         return 'Hubo un error actualizando la simulacion'
   else:
      return render_template('edit.html', credit_to_edit = credit_to_edit)
         
         
@app.route('/simulador', methods=['GET', 'POST'])
def simulador():

   return render_template('simulador.html')

@app.route('/')
def home():
   return render_template('inicioz.html') #inicioz.html
   pass

if __name__ == "__main__":
	app.run(debug=True)