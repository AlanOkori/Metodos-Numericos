Entero = int(input("ingresa un número positivo."))
while Entero <= 0 :
    print ("Debes ingresar un numero positivo.")
    Entero = int(input("ingresa un número positivo."))
cont = 1
while cont < 11 :
    print(Entero, " x " , cont ," = ",(Entero*cont))
    cont = cont +1 