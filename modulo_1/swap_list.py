def swap_list(lista, ind, ind2):
    """
    la funzione prende in input una lista e gli indici che indicano la posizione dei valori
    da scambiare. Poi esegue uno scambio tra tali valori
    """
    tmp= lista[ind2]        #salvo il valore che si trova alla posizione della lista di inice ind2
    lista[ind2]=lista[ind]  #cambio il valore prima salvato con quello che si trova alla posizione ind
    lista[ind]=tmp  #faccio l'effettivo scambio
    
    # lista[ind], lista[ind2] = lista[ind2], lista[ind]

lista=[]
for i in range(5):
    print('Aggiungi elemento alla lista:')
    x=int(input())
    lista.append(x)
for indice, valore in enumerate(lista, ):
    print(f"Indice {indice}: {valore}") #qui sarebbe da stampare la lista, ma con un enumerate che mi indichi l'indice

print('che valori vuoi scambiare? Digita il loro indice')
i= int(input())
j=  int(input())
#sarebbe da gestire il caso in cui gli indici digitati non siano parte della lista
swap_list(lista, i, j)
print(lista)
