def between(Num1, Num2):
    if Num1 > Num2 :
        for Num2 in range (Num2,Num1+1) :
            print(Num2)
    else :
        for Num1 in range (Num1,Num2+1) :
            print(Num1)
            
x = int(input("Please, insert the first number: "))
y = int(input("Please, insert the second number: "))
between(x,y)
input("Press key to continue.")