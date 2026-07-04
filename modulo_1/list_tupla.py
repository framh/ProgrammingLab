

def list_tupla():
    lista = []
    n=0
    while n != -1:
        print('aggingi elemento alla lista:')
        n = int(input())
        if(n != -1):
            lista.append(n)
    
    tupla = tuple(lista)
    print(lista)
    print(tupla)

def serie_list_tupla():
    n = input('inserisci la serie di numeri separati da una virgola:')
    lista = n.split(",")
    tupla = tuple(lista)


list_tupla()