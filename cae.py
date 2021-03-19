def Cuota(caprestado,interes,cCuotas):
    iinteres = interes/100
    cuota = (caprestado*iinteres)/(1-pow(1+iinteres,-cCuotas))
    return cuota


def amortizacion(saldoRestante,cuota,interes):
    amort = cuota-((interes/100)*saldoRestante)
    return amort



def CAE(capitalPrestado, cuotas, interes,seguro):
    #La cuota fija es independiente del seguro, eso se le suma aparte
    cuotaFija = Cuota(capitalPrestado,interes,len(cuotas))


    if seguro == False:
        
        amortizacion(capitalPrestado,len(cuotas),)




if __name__=="__main__":
    cuotas = [12]
    capitalPrestado = 1015714
    interes = 1,2
    seguro = False

    CAE(capitalPrestado, cuotas, interes, seguro)



hola