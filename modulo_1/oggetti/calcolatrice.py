import math

class Calcolatrice():

    def __init__(self):
        pass
    
    def dividi(self, num1, num2):
        try:
            self.num1 = num1
            self.num2 = num2
            risultato = num1/num2
            print(risultato)
            return (risultato)

        except TypeError as e:
            print(f'errore: {e}')
        
        except ValueError as e:
            print(f'errore: {e}')
        
        except ZeroDivisionError as e:
            print(f'errore: {e} Hai inserito uno 0 come dividendo?')
    
    def radice_quadrata(self, num):
        if num <= 0:
            raise ValueError('Accettati solo numeri > di 0!')
        
        radice = math.sqrt(num)
        print(radice)
        return(radice)
    

divisione = Calcolatrice()
divisione.dividi(4,2)
divisione.dividi(4,0)
divisione.dividi(4,"2")
Calcolatrice.radice_quadrata(divisione, 4)
Calcolatrice.radice_quadrata(divisione, 0.4)
Calcolatrice.radice_quadrata(divisione, -4)