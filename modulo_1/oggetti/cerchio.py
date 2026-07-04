

class Circle():
    def __init__(self, raggio):
        self.raggio = int(raggio)
    
    def area(self):
       area = 3.14 * pow(self.raggio,2) 
       print(f'{area}')
       return area

cerchio = Circle(2)
cerchio.area()