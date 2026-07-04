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
        print(f'Frequento il corso:', self.corsi)


class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        print(f"> Docente del corso: ", self.corsi)
    
    

corsi = ['programmazione', 'analisi', 'francese', 'karate']
Irene = Studente('Irene', 'Stefani', corsi)
Irene.saluta()

Paolo = Docente('Paolo', 'Frizzi', corsi)
Paolo.saluta()

