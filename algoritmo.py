import numpy as np
#Cuota mensual fija, con el seguro incluido.

def Cuota(caprestado,interes,cCuotas):
    cuota = (caprestado*interes)/(1-pow(1+interes,-cCuotas))
    return cuota

def interes_mensual(saldo_del_mes,interes):
    i = saldo_del_mes*interes
    return i

def amortizacion(cuota_unica,interes):
    amort = cuota-interes
    return amort

def interes_acumulado(monto_bruto,meses,tasa,cuota):
    acumulador = 0

    for i in range(0,meses):
        interes_periodo = interes_mensual(monto_bruto,tasa)
        print("interes del mes : "+ str(i) + " es " + str(interes_periodo))
        acumulador  = acumulador + interes_periodo
        monto_bruto = monto_bruto - amortizacion(cuota,interes_periodo)
    
    return acumulador

def irr(datos):
    irr = np.irr(datos)
    return irr

def cae(irr,meses):
    return irr*meses*100

def ajustar_interes(interes):
    interes = interes/100
    return interes
    
# def ALgoritmo(data):
#     #[Nombre, Monto, interes,meses, ,gastos asociados,seguro1, seguro2, seguro3,...]
#     nombre = data[0]
#     monto = data[1]

if __name__== "__main__":

    #datos de entrada
    i= 1.2
    meses = 12
    capital = 1000000
    seguro = 4182
    gastosAsociados = 15715

    #ajustamos interes para los calculos:
    i = ajustar_interes(i)
    print("##### " + str(i))
    #monto bruto
    total = capital + seguro + gastosAsociados 

    #datos a colocar en la funcion numpy irr
    datos = []
    #Agregamos el primer dato que es el capital en signo negativo
    datos.append(capital*-1)
    #calculamos la cuota mensual
    cuota= Cuota(total,i,meses) 
    #agregamos la cantidad de veces que sean necesarias (depende de la cantidad de meses)
    for a in range(0,meses):
        datos.append(cuota)
    #calculamos irr
    irr = irr(datos)
    #calculamos cae
    CAE = cae(irr,meses)
    #calculamos intereses acumulados
    acumulados = interes_acumulado(total,meses,i,cuota)
    #calculamos costo total del credito
    costo_total = total + acumulados






    print("Irr = " + str(irr))
    print( "CAE: " + str(CAE) +"%")
    print("interesAcumulado: " + str(acumulados))
    print("Monto Bruto del credito " + str(total))
    print("Costo total " + str(costo_total  ))
    print("Cuota: " + str(cuota))






#print(round)