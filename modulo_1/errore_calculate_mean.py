

def calculate_mean(data):
    
        if not isinstance(data, list):
            raise TypeError('Il tipo inserito non è una lista!')
       
        if data == []:
            raise ValueError('Liste vuote non ammesse!')
        
        if not all(isinstance(x, int) for x in data):
            raise TypeError('La lista contiene almeno un elemento non compatibile con l\'operazione di media')


        virgola = [float(x) for x in data]
        somma = 0
        for i in virgola:
            # if i != float:
            #     raise TypeError
            somma = somma + i
        
        if somma == 0:
            raise ValueError('i dati inseriti sono tutti 0. Impossibile calcolare la media!')

        media = somma/len(virgola)
        print(f'media di {data}: {somma}')
        return(media)
 
try:
    calculate_mean([10, 20, 30])
except ValueError as e:
    print(f"Errore: {e}")   

try:
    calculate_mean([])
except ValueError as e:
    print(f"Errore: {e}")  

try:
   calculate_mean("ciao")
except TypeError as e:
    print(f"Errore: {e}")  

try:
    calculate_mean([10, "venti", 30])
except TypeError as e:
    print(f"Errore: {e}")  





        