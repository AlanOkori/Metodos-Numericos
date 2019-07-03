def AgregarUnaVez(lista, e) :
    try :
        if e in lista :
            raise ValueError
        else :
            lista.append(e)
            return lista
    except ValueError:
        print("Error: Imposible añadir elementos duplicados.")
        return lista
List = [1,2,3,4,5,6]
print("The list is: ", AgregarUnaVez(List,5))