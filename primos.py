Entero = int(input("ingresa un número entero positivo."))
while Entero < 2 :
    print ("Debes ingresar un numero mayor a uno")
    Entero = int(input("ingresa un número entero positivo."))
cont = 1
while cont < Entero :
    cont2 = 2
    esprimo = True
    while cont2 <= cont :
        if cont % cont2 != 0 :
            esprimo = True
        else :
            esprimo = False   
    cont2 = cont2+1
    if esprimo == True:
        print(Entero)
            