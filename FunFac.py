def fact(Num):
    Fac = 1.0
    for i in range (1,Num+1) :
        Fac = Fac * i
    print("The Factorial is: ", Fac)   
x = int(input("Please, insert a number: "))
fact(x)
input("Press key to continue.")