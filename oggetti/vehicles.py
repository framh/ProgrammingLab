
class Vehicles():
   
    def __init__(self, marca, modello, anno, speed):
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


