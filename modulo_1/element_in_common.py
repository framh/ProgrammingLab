def element_in_common(lista, lista2):
    """
    La funzione prende in input due liste distinte, di lunghezze anche diverse e 
    cerca se hanno elementi in comune. Se li trova restituirà TRUE, in caso contrario FALSE
    """
    for elemento in lista:
        if elemento in lista2:
            print('elementi in comune trovati')
            return True
    
    print('non hanno elementi in comune')
    return False

lista=[]
lista2=[]
for i in range(5):
    print('Aggiungi elemento alla lista:')
    x=int(input())
    lista.append(x)

for i in range(5):
    print('Aggiungi elemento alla seconda lista:')
    x=int(input())
    lista2.append(x)

element_in_common(lista,lista2)