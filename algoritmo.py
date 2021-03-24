import numpy as np
#Cuota mensual fija, con el seguro incluido.

def Cuota(caprestado,interes,cCuotas):
    cuota = (caprestado*(interes*pow(1+interes,cCuotas)))/((pow(1+interes,cCuotas)-1))
    return cuota

def interes_mensual(saldo_del_mes,interes):
    i = saldo_del_mes*interes
    return i

def amortizacion(cuota_unica,interes):
    amort = cuota_unica-interes
    return amort

def interes_acumulado(monto_bruto,meses,tasa,cuota):
    acumulador = 0

    for i in range(0,meses):
        interes_periodo = interes_mensual(monto_bruto,tasa)
        # print("interes del mes : "+ str(i) + " es " + str(interes_periodo))
        acumulador  = acumulador + interes_periodo
        monto_bruto = monto_bruto - amortizacion(cuota,interes_periodo)
    
    # print("resto = " + str(monto_bruto))
    return acumulador

def irr(datos):
    irr = np.irr(datos)
    return irr

def cae(irr,meses):
    return irr*meses*100

def ajustar_interes(interes):
    interes = interes/100
    return interes
    
# def algoritmo_edit
# def reestructurar arreglo

def Algoritmo(capital,i,meses,gastosAsociados,seguro):
    #[monto, interes,meses,gastos_asociados,total_seguro]
    

    #ajustamos interes para los calculos:
    i = ajustar_interes(i)
    # print("##### " + str(i))
    #monto bruto
    total = capital + seguro + gastosAsociados 
    # print('total' + str(total))

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
    tir = irr(datos)
    #calculamos cae
    CAE = "{0:.2f}".format(cae(tir,meses)) #Nose si redondear o truncar round(cae(tir,meses),2)
    #calculamos intereses acumulados
    acumulados = interes_acumulado(total,meses,i,cuota)
    #calculamos costo total del credito
    costo_total = total + acumulados

    return tir,CAE,acumulados,total,costo_total,cuota


    

# if __name__== "__main__":

#     tir,CAE,acumulados,total,costo_total,cuota = ALgoritmo(1000000,1.99,12,8839,8589)

#     print('tir : ' + str(tir))
#     print(str(CAE))
#     print(str(int(round(acumulados))))
#     print(str(int(round(total))))
#     print(str(int(round(costo_total))))
#     print(str(int(round(cuota))))












#print(round)