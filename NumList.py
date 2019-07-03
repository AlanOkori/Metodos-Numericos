Number = int(input("Please, insert a number : "))
List = []
while Number != 0 :
    List.append(Number)
    Number = int(input("Please, insert a number. Insert 0 to exit : "))
print("The inserted number list is : ", List)
input("Press a key to continue.")