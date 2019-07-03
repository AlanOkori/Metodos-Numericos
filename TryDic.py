colores = {'rojo' : 'red' , 'verde' : 'green' , 'negro' : 'black'}

try :
    print(colores['blanco'])
except KeyError :
    print("Error: that color doesn't exist on the dictionary.")