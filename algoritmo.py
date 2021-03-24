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

def cae(irr):
    return irr*12*100

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
    CAE = "{0:.2f}".format(cae(tir)) #Nose si redondear o truncar round(cae(tir,meses),2)
    #calculamos intereses acumulados
    acumulados = interes_acumulado(total,meses,i,cuota)
    #calculamos costo total del credito
    costo_total = total + acumulados

    return tir,CAE,acumulados,total,costo_total,cuota


    

if __name__== "__main__":
    #[nombre,monto, interes,meses,gastos_asociados,total_seguro]
    s1 = ['Banco Consorcio',1000000,1.18,12,1000,12324]
    s2 = ['Banco de Chile',1000000,2.26,12,9692,7345]
    s3 = ['Banco Estado',3000000,1.55,24,25219,39697]
    s4 = ['Banco Santander',3000000,2.03,24,27746,65492]
    s5 = ['Banco Estado',5000000,1.25,36,41562,66155]
    s6 = ['Scotiabank Azul',5000000,2.16,36,43603,126640]
    s7 = ['Caja los Andes',7000000,1.10,48,58184,127371]
    s8 = ['Banco Security',7000000,1.58,48,60618,329171]
    s9 = ['Banco de Chile',9000000,1.6,60,76792,327735]
    s10 = ['Caja la Araucana',10000000,1.62,60,81451,1294440]

    simulaciones = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

    for s in simulaciones:
        tir,CAE,acumulados,total,costo_total,cuota = Algoritmo(s[1],s[2],s[3],s[4],s[5])
        print(s[0])
        print('CAE ' + str(CAE) + '% ' + 'Cuota ' + str(costo_total))
        print('\n')

    

    












#print(round)