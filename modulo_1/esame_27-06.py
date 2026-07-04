
class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, nome):
        
        if not isinstance(nome, str):
            raise ExamException("Controllare il tipo del file inserito. Non è una stringa")

        if nome == "":
            raise ExamException("Il nome del file non può essere vuoto")
        
        try:
            with open(nome, 'r') as file:
                self.name = nome
                lista_stati = []
                self.lista_stati = lista_stati
        except FileNotFoundError:
            raise ExamException("file non trovato")
    
    def get_data(self, nome_stato):
        if not isinstance(nome_stato, str):
            raise ExamException("Controllare il tipo dello stato richiesto")
        
        if nome_stato == "":
            raise ExamException("Il nome della città non può essere vuoto")
        
        
        trovato = 0

        with open(self.name, 'r') as file:
            righe = file.readlines()
            #print("RIGHE: ", righe)
            
            for riga in righe:
                eventi = riga.strip().split(',')
                #print("EVENTI: ", eventi)
                data = eventi[0].split("-")
                anno = data[0]
                stato = eventi[2]

                if stato == nome_stato:
                    trovato = 1
                    try:
                        check = float(eventi[1])
                        if check < 0:
                            continue
                        
                        elementi = [eventi[0] , eventi[1]]
                        self.lista_stati.append(elementi)
                    except ValueError:
                        print("Dato viziato o mancante")
                        continue
            if trovato == 0:
                raise ExamException("Lo stato cercato non è presente nei registri")              
            
            #print(self.lista_stati)
            return(self.lista_stati)

def compute_slopes(time_series, first_year, last_year):
    if not isinstance(time_series, list):
        raise ExamException(f"Controllare il tipo di {time_series}") 
    
    if not (isinstance(first_year, int) or isinstance(last_year,int)):
        raise ExamException
    
    if first_year > last_year:
        raise ValueError("Il primo anno dell'intervallo non può essere maggiore delll'ultimo")
    dizionario = {}

    time_series.sort()

    for eventi in time_series:
        data = eventi[0].split('-')
        #print("DATA: ", data)
        anno = data[0]#.split('-')
        #print("ANNO: ", anno)
        valore_float = float(eventi[1])
        anno_intero = int(anno)

        if anno_intero not in range(first_year, last_year+1):
            continue
        
        if anno_intero not in dizionario:
            dizionario.update({anno_intero : [valore_float]})
            print(f"Chiave {anno_intero} creata")
        else:
            dizionario[anno_intero].append(valore_float)
    
    dizionario_media_annuale = {}
    n = 0
    for chiave in dizionario:
        if len(dizionario[chiave]) < 6:
            print(f"Anno {chiave} ha troppi pochi dati per il calcolo")
            continue
        media_anno = sum(dizionario[chiave])/len(dizionario[chiave])  
        dizionario_media_annuale.update({chiave : media_anno})  

        n = n+1
    
    if n == 0:
        raise ExamException("Il numero di anni è troppo piccolo per l'intervallo richiesto")

    somma_value = 0
    somma_anno = 0
    for chiave in dizionario_media_annuale:
        somma_value = somma_value + dizionario_media_annuale[chiave]
        somma_anno = somma_anno + chiave
    

    media_value = somma_value / n
    media_anno = somma_anno / n
    # print(f"MEDIA_V: {media_value}")
    # print(f"MEDIA_A: {media_anno}")

    # sommatoria_anni = 0
    # sommatoria_temperatura = 0
    sommatoria_numeratore = 0
    sommatoria_denominatore = 0
    for chiave in dizionario_media_annuale:
        # sommatoria_anni = sommatoria_anni + (chiave - media_anno)
        # sommatoria_temperatura = sommatoria_temperatura + (dizionario_media_annuale[chiave] - media_value)
        sommatoria_numeratore = sommatoria_numeratore + (chiave - media_anno) * (dizionario_media_annuale[chiave] - media_value)
        sommatoria_denominatore = sommatoria_denominatore + pow((chiave - media_anno), 2)
    
    # print(f"SOMMATORIA_A: {sommatoria_anni}")
    # print(f"SOMMATORIA_T: {sommatoria_temperatura}")
    #print(f"SOMMATORIA_D: {sommatoria_denominatore}")
    if sommatoria_denominatore == 0:
        raise ExamException("Errore: Il denominatore è uguale a 0!")
    coefficciente_angolare = sommatoria_numeratore/ sommatoria_denominatore
    print("COEFFICIENTE ANGOLARE", coefficciente_angolare)
    return(coefficciente_angolare)


    


        
        

docs = CSVTimeSeriesFile("Globallandtemperaturesbycountry.csv")
contenuto = docs.get_data("Italy")
compute_slopes(contenuto, 1900, 1902)
        