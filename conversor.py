tipo_moneda = input("Ingrese el tipo de moneda que tiene :\n1.\t Pesos\n2.\tdolares\n")
if tipo_moneda == "1" :
    tipo_moneda = "Pesos"
    pesos = input("¿Cuantos Pesos tiene?\n")
    pesos =float(pesos)
    valor_dolar = 4000
    dolar = round(pesos / valor_dolar,2)
    dolar = str(dolar)
    print(" Usted tiene $ " + dolar + " dolares")
elif tipo_moneda == "2" :
    dolar = input("¿Cuantos Dolares tiene?\n")
    dolar =float(dolar)
    valor_dolar = 4000
    pesos = round(dolar * valor_dolar,2)
    pesos = str(pesos)
    print(" Usted tiene " + pesos + " pesos")
else :
    print("hola")
    exit()



