
class Vehicles():
   
    def __init__(self, marca, modello, anno, speed = 0):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        #self.speed = speed
        self.speed=0
    
    def __str__(self):
        print(' marca: ', self.marca , 
        '\n modello:' , self.modello, 
        '\n anno:', self.anno, 
        '\n speed:', self.speed)
       
    def acceleration(self, speed):
        self.speed = self.speed + 5
   
    def brake(self, speed):
        self.speed = self.speed - 5
    
    def get_speed(self, speed):
        print('la speed corrente è:', self.speed)
        return(self.speed)
    
class car(Vehicles):    #sottoclasse macchina

        def __init__(self, modello, marca, anno, numero_porte):
            super().__init__(modello, marca, anno)
            self.numero_porte = numero_porte

        def __str__(self)  :
            match self.numero_porte:
                case 5:
                        print(f'la tua {self.marca} {self.modello} ha {self.numero_porte}')
                        return(f'la tua macchina ha {self.numero_porte}')

                case 0 | 1 | 2 | 3 | 4:
                        print(f'la tua {self.marca} {self.modello} ha {self.numero_porte}, probabilmete è una smart o non ha il bagagliaio o ti hanno rubato qualche porta.')
                        return(f'la tua macchina ha {self.numero_porte}, probabilmete è una smart o non ha il bagagliaio o ti hanno rubato qualche porta.')
            
class motorcycle(Vehicles): #sottoclasse moto
        def __init__(self, tipo):
            self.tipo = tipo
        
        def __str__(self):  
            base = super().__str__()
            return f'{base}\n tipo: {self.tipo}'
        

Bmw = Vehicles('bmw', 'x3', 2001, 30)
Vehicles.__str__(Bmw)
Vehicles.acceleration(Bmw, 30)
Vehicles.brake(Bmw, 30)
Vehicles.acceleration(Bmw, 30)
Vehicles.get_speed(Bmw, 30)

Audi = Vehicles('audi', 'a1', 2011, 70)
Vehicles.__str__(Audi)
Vehicles.acceleration(Audi, 70)
Vehicles.brake(Audi, 70)
Vehicles.acceleration(Audi, 70)
Vehicles.get_speed(Audi, 70)

Fiat = car('fiat', '500', 2001, 4)
car.__str__(Fiat)

