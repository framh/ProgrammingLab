import random #con questo ci generi numeri casuali
import copy #con questo puoi copiare le classi
            #ricorda copy e deepcopy

class coin():
    def __init__(self, faccia):
        self.faccia = faccia
    def lanciare(self):
        if random.randint(0,1) == 0: 
         self.faccia = "testa"
        else:
            self.faccia = "croce"
    
    def result(self):
        return self.faccia

#creo ora l'oggetto vero e proprio
euro= coin('Testa')
coin.lanciare(euro)
print(coin.result(euro))

sterlina= coin('Testa')
coin.lanciare(sterlina)
print(coin.result(sterlina))

yen= coin('Testa')
coin.lanciare(yen)
print(coin.result(yen)) 
#avendo 3 oggetti diversi, con 3 nomi diversi, le caratteristiche di coin vengono applicate a tutti



