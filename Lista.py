List = []
Number = int(input(" Please insert a number higher than 1."))
while Number < 1 :
    print (" The number must be higher than 1.")
    Number = int(input(" Insert a number higher than 1."))
 
for i in range (1,Number+1) :
    List.append(i)
print (" The full list is: ", List)
input(" Key to continue")