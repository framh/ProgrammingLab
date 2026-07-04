

def multiplo_3():
    lista = []
 
    for i in range( 0, 1001):
     
        if i % 3 == 0 and i % 5 != 0:
         
            lista.append(str(i))
    
    stringa = " , ".join(lista)
    print(stringa)
    return(stringa)

multiplo_3()