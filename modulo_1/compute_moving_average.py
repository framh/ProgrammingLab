

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        if not isinstance(name, str): #controllo che il tipo del nome del file sia corretto
            raise ExamException("controlla il tipo del file")
        
        if name == "": #controllo che la stringa del nome non sia vuota
            raise ExamException("Il nome del file è vuoto")
        
        try:
            with open(name, 'r') as file:
                self.name = name
        
        except FileNotFoundError:
            raise ExamException("Il file non è stato aperto")
    
    def get_data(self):
        listone = []

        with open(self.name, 'r') as file: #apro il file con il with, così posso non preoccuparmi di chiuderlo
            righe = file.readlines()

            for riga in righe[1:]: #salto la prima riga d'intestazione e divido il file nei dati che mi servono iternado sulle singole righe
                eventi = riga.strip().split(",")
                #print(f"EVENTI: {eventi}")
                data = eventi[0].split("-")
                #print(f"DATA: {data}")
                anno = data[0]
                anno_intero = int(anno)
                
                try: #con il try provo a convertire il valore associato alla data, se non ci riesco, vuol dire che il tipo è sbagliato e quindi scatta l'eccezione
                    check = float(eventi[1])
                    if check < 0: #ignoro la riga se il dato è negativo
                        continue
                    listone.append([eventi[0], check]) #inizio a creare la lista di li liste 
                except ValueError:
                    print("dato viziato o mancante")
        print(listone)
        return(listone)

def compute_moving_average(time_series, first_year, last_year, N):
    if not isinstance(time_series, list):   #controllo che il tipo della serie sia corretto
        raise ExamException("controllare il tipo della serie")

    if time_series == []: #controllo che la lista della serie non sia vuota
        raise ExamException("La serie inserita è vuota")
    
    if not (isinstance(first_year, int) and isinstance(last_year, int)): #controllo che il tipo degli estremi sia corretto
        raise ExamException("controllare il tipo degli estemi dell'intervallo")
    
    if first_year > last_year: #controllo che l'intrevallo sia valido
        raise ExamException("L'estremo inferiore non può essere superiore dell'estremo superiore")
    
    if not isinstance(N, int): #controllo che il tipo del numero di anni arretrati da controllare sia corretto
        raise ExamException("controllare il tipo del valore N")
    
    if N <= 0: #se N non è positivo e maggiore di zero, risulta impossibile controllare gli anni precedenti, quindi verifico che lo sia effettivamente
        raise ExamException("Il valore di N non può essere <0")
    
    if N > (last_year-first_year):
        raise ExamException("Il numero degli anni richiesti non può essere maggiore dell'intervallo esaminato")
    
    dizionario_anno = {}
    for eventi in time_series: #con questo for creo effettivamente il dizionario con gli anni appartenenti al range d'interesse
        #print(f"EVENTI: {eventi}")
        data = eventi[0].split("-")
        #print(f"DATA: {data}")
        anno = data[0]
        #print(f"ANNO: {anno}")
        anno_intero = int(anno)
        if anno_intero not in range(first_year, last_year+1):
            continue
        
        if anno_intero not in dizionario_anno:
            dizionario_anno.update({anno_intero : [eventi[1]]})
        else:
            dizionario_anno[anno_intero].append(eventi[1])
    
    dizionario_media = {}
    for anno in dizionario_anno: #qui creiamo il secondo dizionario con la sottrazione tra la media dell'anno meno la media delle medie degli anni precedenti
        check = 1 #valore flag per capire se esistono abbastanza anni arretrati
        countdown = N #così N lo lascio intatto 
        somma = 0

        while countdown != 0: #controllo se esistono effettivamente questi anni
            if (anno-countdown) not in dizionario_anno: #non c'è un anno, il processo salta e l'anno viene ignorato
                check = 0 #ignorato grazie a questo valore flag che si aggionra
                break
            else:
                media = sum(dizionario_anno[anno-countdown])/len(dizionario_anno[anno-countdown])
                somma = somma + media
                countdown = countdown - 1 

        if check == 1: #se il flag resta invariato, ergo esistono tutti gli anni precedenti che mi interesano, avviene la sottrazione effettiva
            media = (sum(dizionario_anno[anno])/len(dizionario_anno[anno])) - somma/N
            dizionario_media.update({anno : media})
    print(f"D_MEDIA: {dizionario_media}")
    return(dizionario_media)

docs = CSVTimeSeriesFile("precipitazioni2.csv")
lista = docs.get_data()
compute_moving_average(lista, 2000, 2004, 2)