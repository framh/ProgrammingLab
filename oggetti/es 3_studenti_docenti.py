class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)
    
    def corso(self, corsi):
        self.corsi = corsi
    

class Studente(Persona):

    # costruttore sotto-classe
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi

    # ridefinizione del metodo bonjour di persona
    def saluta(self):
        Persona.saluta(self)  # uso esplicitamente metodo di Persona
        print(f'Frequento il corso:', self.corsi, '\n')
    
    def qualcuno_insegna(self):
        j = 0
        for indx in self.corsi:

            for i in lista_docenti:
                if indx in i:
                    print(f'trovato insegnante per {indx} \n')
                    break
               
            

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
        lista_docenti.append(corsi)

    def saluta(self):
        Persona.saluta(self)
        print(f"> Docente del corso: ", self.corsi, '\n')
    
    def stessi_corsi(self, studente):
        corsi = self.corsi
        st_corsi = studente.corsi
        sorted(corsi)
        sorted(st_corsi)
        gate = 0
        for indx in corsi:
            gate = 0

            for i in st_corsi:
                if indx == i: #correggere il fatto che si ferma solo al primo controllo
                            #si potrebbero o riordinare le liste in ordine alfabetico così che 
                            # questo controllo possa avere senso
                            # o bisogna cambiare la posizione di check
                    gate = 1
            
            if gate == 0:
                print('non seguono gli stessi corsi')
                return

        
        print('effettivamente seguono gli stessi corsi')
        return

lista_docenti = []
corsi = ['programmazione', 'filosofia', 'scacchi', 'karate', 'golf']
Irene = Studente('Irene', 'Stefani', corsi)
Irene.saluta()

corsi = ['analisi', 'programmazione', 'judo', 'francese']
Paolo = Docente('Paolo', 'Frizzi', corsi)
Paolo.saluta()

Paolo.stessi_corsi(Irene)

corsi = ['scacchi', 'matematica']
Gino = Docente('Gino', 'Frizzi', corsi)
corsi = ['biologia', 'filosofia', 'economia']
Matteo = Docente('Matteo', 'Loris', corsi)

Irene.qualcuno_insegna()