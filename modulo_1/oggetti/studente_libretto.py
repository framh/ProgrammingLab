

class Studente():

    def __init__(self, nome, matricola):
        if not isinstance(matricola, int):
            raise TypeError('Errore nell\'inserimento del numero di matricola, controllare il tipo inserito.')
        if nome == '':
            raise ValueError('Il nome non può essere lasciato vuoto!')
        self.name = nome
        self.matricola = matricola
        
        libretto = []
        self.libretto = libretto
        
        somma = 0
        self.somma = 0
    
    def aggiungi_voto(self, voto):
        
        if not isinstance(voto, int):
            raise TypeError('Errore nell\'inserimento del voto. Controllare il tipo inserito.')

        if voto < 18 or voto > 30:
            raise ValueError('Il voto è insufficiente per essere aggiunto al libretto!')
        
        
        libretto = self.libretto
        libretto.append(voto)
        print('Voto aggiunto al libretto!')
        self.somma = voto + self.somma
    
    def media_voti(self):
        if self.somma == 0:
            raise ValueError('Lo studente non ha voti registrati')

        media = self.somma/len(self.libretto)
        self.media = media
        print(f'la media è {self.media}')

voto = 0
Irene = Studente('Irene', 101)
while voto != -1:
    voto = int(input('inserire il voto dello studente: '))
    if voto != -1:
        try:
            Irene.aggiungi_voto(voto)
        except ValueError as e:
            print(f'errore {e}')

Irene.media_voti()

Paolo = Studente('Paolo', 102)
try: 
    Paolo.aggiungi_voto(18)
except ValueError as e:
    print(f'errore {e}')
try: 
    Paolo.aggiungi_voto(25)
except ValueError as e:
    print(f'errore {e}')
try: 
    Paolo.aggiungi_voto(30)
except ValueError as e:
    print(f'errore {e}')
try: 
    Paolo.aggiungi_voto(17)
except ValueError as e:
    print(f'errore {e}')
Paolo.media_voti()

# Usando una lista degli studenti posso sapere mentre aggiungo i voti a chi li sto aggiungendo
# studenti = [Irene, Paolo] 
# for studente in studenti:
#     voto = 0
#     while voto != -1:
#         voto = int(input(f'inserire il voto di {studente.name}: '))
#         if voto != -1:
#             try:
#                 studente.aggiungi_voto(voto)
#             except ValueError as e:
#                 print(f'errore {e}')