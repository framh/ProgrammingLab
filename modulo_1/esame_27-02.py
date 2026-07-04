

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        
        if not isinstance(name, str):
            raise ExamException("Controllare il tipo del file")
        if name == "":
            raise ExamException("Il nome del file non può essere lasciato vuoto")
        
        try:
            with open(name, 'r') as file:
                self.name = name
                listone = []
                self.listone = listone

        except FileNotFoundError:
            raise ExamException("errore: il file non è stato aperto")
    
    def get_data(self, nome_stato):
        if not isinstance(nome_stato, str):
            raise ExamException("controllare il tipo del nome dello stato")
        if nome_stato == "":
            raise ExamException("Lo stato non può essere lasciato vuoto")
        
        listone = []
        trovato = 0
        with open(self.name, 'r') as file:
            righe = file.readlines()
            
            for riga in righe[1:]:
                eventi = riga.strip().split(",")
                #print(f"EVENTI: {eventi}")
                data = eventi[0].split("-")
                anno = data[0]
                anno_intero = int(anno)

                
                try: 
                    check = float(eventi[1])
                    if check < 0:
                        continue
                    if nome_stato == eventi[2]:
                        trovato = 1
                        elementi = [eventi[0], check]
                        listone.append(elementi)
                except ValueError:
                    print("dato viziato o mancante")
                    continue
            if trovato == 0:
                raise ExamException("lo stato ricercato non è presente nei registri")
            
        print(f"LISTONE DI {nome_stato} {listone}")
        return(listone)

def compute_variations(time_series_1, time_series_2, first_year, last_year):
    if not( isinstance(time_series_1, list) and isinstance(time_series_2,list)):
        raise ExamException("controlla il tipo delle serie")
    
    if not( isinstance(first_year, int) or isinstance(last_year, int)):
        raise ExamException("controlla il tipo dell'intervallo")
    
    if first_year > last_year:
        raise ExamException("L'inizio dell'intervallo non può essere superiore della fine")
    
    dizionario_anno = {}

    for eventi in time_series_1:
        data = eventi[0].split("-")
        anno = data[0]
        anno_intero = int(anno)

        if anno_intero in range(first_year, last_year+1):
            if anno_intero not in dizionario_anno:
                dizionario_anno.update({anno_intero : [eventi[1]]})
            
            else:
                dizionario_anno[anno_intero].append(eventi[1])
    print(f"D-ANNO 1: {dizionario_anno}")

    dizionario_anno_2 = {}
    for eventi in time_series_2:        #aggiungiamo per gli stessi anni i valori della seconda serie
        data = eventi[0].split("-")
        anno = data[0]
        anno_intero = int(anno)

        if anno_intero in range(first_year, last_year+1):
            if anno_intero not in dizionario_anno_2:
                dizionario_anno_2.update({anno_intero : [eventi[1]]})
            
            else:
                dizionario_anno_2[anno_intero].append(eventi[1])
    print(f"D-ANNO 2: {dizionario_anno_2}")

    dizionario_media_anno_1 = {}
    dizionario_media_anno_2 = {}

    for anno in dizionario_anno:
        media = sum(dizionario_anno[anno])/len(dizionario_anno[anno])
        dizionario_media_anno_1.update({anno : media})
    
    for anno in dizionario_anno_2:
        media = sum(dizionario_anno_2[anno])/len(dizionario_anno_2[anno])
        dizionario_media_anno_2.update({anno : media})
    print(f"ANNO 1: {dizionario_media_anno_1}")
    print(f"ANNO 2: {dizionario_media_anno_2}")

    dizionario_variazione_annuale = {}
    for anno in dizionario_media_anno_1:
        if anno not in dizionario_media_anno_2:
            continue
        variazione = dizionario_media_anno_2[anno] - dizionario_media_anno_1[anno]
        dizionario_variazione_annuale.update({anno : variazione})
    
    print(dizionario_variazione_annuale)
    return(dizionario_variazione_annuale)
    

    
    
    

docs = CSVTimeSeriesFile("Globallandtemperaturesbycountry2.csv")
Italia = docs.get_data("Italy")
Francia = docs.get_data("France")
compute_variations(Italia, Francia, 1900, 1902)

    


        