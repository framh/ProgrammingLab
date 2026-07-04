

class Shape():
    
    def __init__(self, lenght):
        self.lenght = int(lenght)
    
    def area(self):
        aShape = 0
        print(aShape)
        return (aShape)

class Square(Shape):

    def __init__(self, lenght):
       super().__init__(lenght)
    
    def area(self):
        aSquare = pow(self.lenght,2)
        print(aSquare)
        return(aSquare)

forma = Shape(4)
quadrato = Square(6)

forma.area()
quadrato.area()