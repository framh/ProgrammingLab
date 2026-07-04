

class Analizzatori_voti():
    def __init__(self, nome):
        if nome == '':
            raise TypeError('Errore: Il nome non può essere lasciato vuoto')
        self.name = nome
        registro = []
        self.registro = registro
    
    def get_data(self):
        try:
            with open(self.name, 'r') as file:
                contenuto = file.read()
                lista = contenuto.split()
                print(lista)
                for i in lista:
                    elementi = i.split(',')
                    self.registro.append(elementi)
                print(self.registro)
                return(self.registro)
        except FileNotFoundError:
            print(f'Errore: il file {self.name} non può essere aperto o non esiste!')
    
    def media_studenti(self, nome_studente):
        if not isinstance(nome_studente, str):
            raise TypeError('controlla il tipo del nome inserito')
        
        if nome_studente == '':
            raise TypeError('Errore: Il nome dello studente non può essere lasciato vuoto')
        
        somma = 0
        counter = 0
        trovato = 0
        
        for index in range(len(self.registro)):
            

            if nome_studente in self.registro[index]:
                trovato = 1

                for interno in self.registro[index]:
                    try: 
                        somma = somma + int(interno)
                        counter +=  1
                    except ValueError:
                        print('questo dato non può essere convertito in intero')
                
                if len(self.registro[index]) == 0:
                    raise ZeroDivisionError(f'Non è possibile dividere per 0. La media per {nome_studente}, non è calcolabile')
                
                media = somma/counter
    
        if trovato != 1:
            raise ValueError('lo studente inserito non compare nei registri, ricontrollare il nome inserito')
        
        print(f'la media è {media}')
        return(media)
    
voti = Analizzatori_voti('voti.csv')
voti.get_data()
voti.media_studenti('Irene')
try:
    voti.media_studenti('Mario')
except ValueError as e:
    print(f'{e}')
