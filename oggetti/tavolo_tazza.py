class Cup():

    def __init__(self, altezza, diametro, asse_x, asse_y):
        self.altezza = altezza
        self.diametro = diametro
        print(f'Tazza di larghezza: {self.diametro} e altezza: {self.altezza} creato \n')
        
        self.asse_x = asse_x
        self.asse_y = asse_y
        print(f'punto d appoggio creato a coordinate: x = {self.asse_x} e y = {self.asse_y}')
        
        self.surface = {
        "x_min": self.asse_x,
        "x_max": self.asse_x + self.diametro,
        "y":     self.asse_y + self.altezza,
        "surface_top": range((self.asse_x + self.altezza), (self.asse_x + self.diametro + self.altezza)),
        "surface_base": range((self.asse_x), (self.asse_x + self.diametro))
        }

    def collide(self, obj_x, obj_y):
        return obj_x in self.tavola["surface_base"] and obj_y == self.tavola["y"]


    def posizione(self, asse_x, asse_y):
        self.asse_x = asse_x
        self.asse_y = asse_y
    
    def move(self, asse_x, asse_y):
        self.asse_x += asse_x
        self.asse_y += asse_y
        print(f'la Tazza si trova a x: {self.asse_x} e a y: {self.asse_y} \n')
    
    def collide(self, obj_x, obj_y):
        return obj_x in self.tavola["surface"] and obj_y == self.tavola["y"]

class Table():

    def __init__(self, larghezza_latoSx, larghezza_latoDx, altezza_piede, altezza_tavola,
                asse_x, asse_y):
        self.altezza = abs(altezza_tavola - altezza_piede)
        self.larghezza = abs(larghezza_latoSx - larghezza_latoDx)
        print(f'tavolo di larghezza: {self.larghezza} e altezza: {self.altezza} creato \n')

        self.asse_x = asse_x
        self.asse_y = asse_y
        print(f'punto d appoggio creato a coordinate: x = {self.asse_x} e y = {self.asse_y}')

        self.tavola = {
        "x_min": self.asse_x,
        "x_max": self.asse_x + self.larghezza,
        "y":     self.asse_y + self.altezza,
        "surface": range((self.asse_x + self.altezza), (self.asse_x + self.larghezza + self.altezza))
        }
        #self.tavola = [(self.asse_y + self.altezza) : (self.asse_x + larghezza_latoDx + self.altezza)]
    
    def collide(self, obj_x, obj_y):
        return obj_x in self.tavola["surface"] and obj_y == self.tavola["y"]
        
    
    def move(self, asse_x, asse_y):
        self.asse_x += asse_x
        self.asse_y += asse_y
        print(f'il tavolo si trova a x: {self.asse_x} e a y: {self.asse_y} \n')
    
    def punto_appoggio_medio(self):
        self.punto_appoggio_medio = int(abs((self.larghezza / 2) + self.asse_x))
        print(f'il punto d\'appoggio medio è a coordinata x: {self.punto_appoggio_medio}')

    

    


Tavolo = Table(0, 6, 0, 1, 1, 0)
Tazza = Cup(1,1)

x = -1
y = -1
while x != 0 or y != 0:
    print('quanto vuoi muovere il tavolo sull\'asse x? ')
    x=(int(input()))

    print('quanto vuoi muovere il tavolo sull\'asse y?')
    y=(int(input()))
    Table.move(Tavolo,x,y)

Table.punto_appoggio_medio(Tavolo)

