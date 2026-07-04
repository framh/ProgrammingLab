

def register_user(nome, età):
    if età < 0:
        raise ValueError('l\'età non può essere negativa!')
       
    
    if nome == "":
        raise ValueError('Devi inserire almeno un carattere per il nome!')
        
    
    print(f'User {nome} registrato con successo!')
    return(1)

try:
    register_user("Gio", 25)
except ValueError as e:
    print(f"Errore: {e}")

try:
    register_user("", 25)
except ValueError as e:
    print(f"Errore: {e}")

try:
    register_user("Gio", -5)
except ValueError as e:
    print(f"Errore: {e}")
    
    

    
