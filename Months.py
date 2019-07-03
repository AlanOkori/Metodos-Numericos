Months = ['January', 'February', 'March', 'April', 'May', 'June']
Months.extend([ 'July', 'August', 'September', 'October', 'November', 'December'])
Search = int(input(" Please insert the number according to the Month."))
while Search < 1 or Search > 12:
    print (" The number must be between 1 and 12. ")
    Search = int(input(" Please insert the number according to the Month."))
print ("The month according to the index is: ", Months.pop(Search-1))
input(" Key to continue")