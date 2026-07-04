

def read_element(lista, ind):
    try:
        print(lista[ind])
    
    except IndexError:
        print('indice inserito fuori range')
    except TypeError:
        print('l\'indice inserito non è un intero!')

read_element([10, 20, 30], 1)    # caso normale
read_element([10, 20, 30], 5)    # indice fuori range
read_element([10, 20, 30], "1")  # indice sbagliato