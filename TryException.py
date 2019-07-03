def Division() :
        a = int(input("Please, insert the first number: "))
        b = int(input("Please, insert the second number: "))
        try:
            div = a/b
            print("The division is: ",div)
        except ZeroDivisionError:
            print("Error: Can't share your apples if you don't have friends")
        except TypeError:
            print("Error: can't divide numbers with characters")
    
Division()