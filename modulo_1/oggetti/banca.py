

class Banca():

    
    def __init__(self, nome_banca):
        self.nome_banca = nome_banca
        maiuscolata = nome_banca.upper()
        print(f'banca {maiuscolata} creata')
        registro = {}
        self.registro = registro
    
    def aggiungi_conto(self, nome, saldo_iniziale):
        if not (isinstance(nome, str) or isinstance(saldo_iniziale, int)):
            raise TypeError('Errore: controllare il tipo dei dati inseriti.')
        
        if nome == '':
            raise ValueError('Il nome non può essere lasciato vuoto!')
        
        if saldo_iniziale <= 0:
            raise ValueError('Il saldo iniziale deve essere maggiore di 0!')
        
        self.name = nome
        self.saldo_iniziale = saldo_iniziale
        self.registro.update({nome : saldo_iniziale})
        print('Conto corrente creato!')
    
    def deposita(self, nome, importo):
        if not (isinstance(nome, str) or isinstance(importo, int)):
            raise TypeError('Errore: controllare il tipo dei dati inseriti.')
        
        if nome == '':
            raise ValueError('Il nome non può essere lasciato vuoto!')
        
        if nome not in self.registro:
            raise ValueError('Il nome inserito non è presente nei registri. Non è registro in nessuna banca.')
        
        if importo <= 0:
            raise ValueError('Impossibile aggiungere questo importo al conto. Riprovare con un importo > 0')
        
        self.registro[nome] = self.registro[nome] + importo
        print(f'Aggiunti a {nome} {importo} fondi')
    
    def preleva(self, nome, importo):
         if not (isinstance(nome, str) or isinstance(importo, int)):
            raise TypeError('Errore: controllare il tipo dei dati inseriti.')
        
         if nome == '':
            raise ValueError('Il nome non può essere lasciato vuoto!')

         if nome not in self.registro:
            raise ValueError('Il nome inserito non è presente nei registri. Non è registro in nessuna banca.')
        
         if importo <= 0:
            raise ValueError('Impossibile prelevare questo importo dal conto. Riprovare con un importo > 0')
        
         if importo > self.registro[nome]:
            raise ValueError('Impossibile prelevare l\'ammontare richiesto. Fondi insufficienti')
        
         self.registro[nome] = self.registro[nome] - importo
         print(f'Prelevati dal conto di {nome}, {importo} fondi')
        
    
    def saldo(self, nome):
        if nome == '':
            raise ValueError('Il nome non può essere lasciato vuoto!')

        if nome not in self.registro:
            raise ValueError('Il nome inserito non è presente nei registri. Non è registro in nessuna banca.')
        
        conto_attuale = self.registro[nome]
        print(f'Attualmente il conto di {nome} ha esattamente {conto_attuale} fondi')
    

Banconi = Banca('banconi')
Banconi.aggiungi_conto('Irene', 100)
Banconi.saldo('Irene')
Banconi.deposita('Irene', 200)
Banconi.preleva('Irene', 50)
Banconi.saldo('Irene')

Banconi.aggiungi_conto('Paolo', 100)
Banconi.saldo('Paolo')
Banconi.deposita('Paolo', 500)
Banconi.preleva('Paolo', 25)
Banconi.saldo('Paolo')

Banconi.preleva('Irene', 50)
Banconi.saldo('Irene')

Banconi.aggiungi_conto('Luca', 0)
Banconi.saldo('Luca')

Banconi.aggiungi_conto('Luca', 10)
Banconi.preleva('Luca', 50)

Banconi.deposita('Luca', 200)
Banconi.deposita('Luca', -5)

Banconi.saldo('Luca')