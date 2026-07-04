
class Poligono():
        def __init__(self, lati):
            self.lati = lati
        
        def __str__(self):
            print(f'sono un poligono con {self.lati} \n')

class Quadrilatero(Poligono):
      def __init__(self, lati):
        self.lati = super().__init__(lati)
        
        if self.lati != 4:
            print('non può essere un quadrilatero!')
            return False
        print('sono un quadrilatero \n')

class Rettangolo(Quadrilatero):
    def __iniit__(self,base,altezza):
        self.base = base
        self.altezza = altezza
        self.lati = super().__init__(lati)
        
        if self.lati != 4:
            print('non può essere un quadrilatero!')
            return False
        print('sono un quadrilatero \n')
    
    def __str__ (self):
        print(f'sono un rettangolo di {self.base} e altezza {self.altezza}')

class Triangolo(Poligono):
    def __init__(self, lati):
        self.lati = lati
        if self.lati != 3:
                print('non può essere un triangolo!')
                return False
                
    def __str__(self):
        return(f'sono un triangolo di {self.lati}')
    
    def perimetro(self, lato_1, lato_2, lato_3):
        perimetro = lato_1 + lato_2 + lato_3
        self.perimetro = perimetro
    
    def is_equilatero(self):
        if self.perimetro % 3 != 0:
            print('non equilatero')
            return(False)

        print('equilatero')
        return True

    
    
        