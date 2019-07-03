Number = int(input("Please, insert a number."))
List = []
while Number <= 0 :
    print ("The number must be higher than 0.")
    Number = int(input("Please, insert a number."))
cont = 1
while cont < 11 :    
    List.append(cont * Number)
    cont = cont +1 
print (List)
input("Press a key to continue.")