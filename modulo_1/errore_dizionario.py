

def leggi_valore(dizionario, key):
    try: 
        print(dizionario[key])
    
    except KeyError:
        print('Questa chiave non esiste')
    
    except TypeError: 
        print(f'{dizionario} non è un dizionario')


leggi_valore({"nome": "Gio", "età": 25}, "nome")   # caso normale
leggi_valore({"nome": "Gio", "età": 25}, "altezza") # chiave assente
leggi_valore([1, 2, 3], "nome")                     # tipo sbagliato