

def leggi_file(docs):
    try:
        with open(docs, 'r', encoding="latin-1") as file:
            contenuto = file.read()
            print(contenuto)

    except TypeError as e:
        print(f"Errore: {e}")  
        print('c\'è un errore nel tipo del file')
    
    except FileNotFoundError as e:
        print(f"Errore: {e}") 
    
    except OSError as e:
        print(f"Errore: {e}") 

leggi_file('esistente.txt')
leggi_file("inesistente.txt")
leggi_file(123)
