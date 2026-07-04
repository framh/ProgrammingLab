

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        if not isinstance(name, str):
            raise ExamException("Controlla il tipo del nome del file")
        
        if name == '':
            raise ExamException("Il nome del file non può essere vuoto")
        
        try:
            with open(name, 'r') as file:
                self.name = name
        
        except FileNotFoundError:
            raise ExamException("Il file non è stato aperto")
    
    def get_data(self):
        listone = []
        with open(self.name, 'r') as file:
            righe = file.readlines()

            for riga in righe[1:]:
                eventi = riga.strip().split(",")
                #print(f"EVENTI: {eventi}")
                data = eventi[0].split("-")
                #print(f"DATA: {data}")
                try:
                    check = float(eventi[1])
                    if check < 0:
                        continue
                    listone.append([eventi[0], check])
                except:
                    continue
            #print(listone)
            return(listone)

def compute_variations(time_series, first_year, last_year):
    if not isinstance(time_series, list):
        raise ExamException("controllare tipo della serie")
    
    if not (isinstance(first_year, int) and isinstance(last_year, int)):
        raise ExamException("controllare tipo degli estremi dell'intervallo")
    
    if first_year > last_year:
        raise ExamException("L'inizio dell'intervallo non può essere successivo alla fine")
    
    dizionario_anni = {}

    for eventi in time_series:
        data = eventi[0].split("-")
        anno = data[0]
        anno_intero = int(anno)
        if anno_intero in range(first_year, last_year+1):

            if anno_intero not in dizionario_anni:
                dizionario_anni.update({anno_intero : [eventi[1]]})
            else:
                dizionario_anni[anno_intero].append(eventi[1])
    print(f"DIZIONARIO_ANNI: {dizionario_anni}")

    dizionario_media_passeggeri = {}
    for anno in dizionario_anni:
        media = sum(dizionario_anni[anno])/len(dizionario_anni[anno])
        dizionario_media_passeggeri.update({anno : media})
    
    dizionario_sottrazione = {}
    for anni in dizionario_media_passeggeri:
        # if (anni - 1) not in dizionario_media_passeggeri:
        #     print(f"anno preccedente assente. Anno {anni} saltato")
        #     continue
        if (anni - 1) not in dizionario_media_passeggeri:
            minnore_anni = min(dizionario_media_passeggeri)
            if minnore_anni == anni:
                continue
            try:
                anno_successivo = anni
                anno_precedente = anni-1
                trovato = 0
                while trovato != 1:
                    if anno_precedente in dizionario_media_passeggeri:
                        trovato = 1
                        sottrazione = dizionario_media_passeggeri[anni] - dizionario_media_passeggeri[anno_precedente]
                        key = str(anno_precedente) + "-" + str(anni)
                        dizionario_sottrazione.update({key : sottrazione})
                    
                    else:
                        anno_precedente = anno_precedente - 1
            except:
                print(f"Non sono stati trovati anni precedenti a {anni}")
                continue
        
        else:
            sottrazione = dizionario_media_passeggeri[anni] - dizionario_media_passeggeri[anni-1]
            key = str(anni-1) + "-" + str(anni)
            dizionario_sottrazione.update({key : sottrazione})
    print(f"DIZIONARIO FINALE: {dizionario_sottrazione}")
    return(dizionario_sottrazione)

def compute_moving_average(time_series, first_year, last_year, N):
    if not isinstance(time_series, list):
        raise ExamException("Controlla il tipo della time_series") 

    if not (isinstance(first_year, int) and isinstance(last_year, int)):
        raise ExamException("Controlla il tipo degli estremi")    
    
    if first_year > last_year:
        raise ExamException("L'inizio dell'intervallo non può essere superiore della fine")
    dizionario_anno = {}

    time_series.sort()
    for eventi in time_series:
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
    
    print(f"D_ANNO: {dizionario_anno}")
    dizionario_media = {}
    for anni in dizionario_anno:
        check = 1
        countdown = N
        somma = 0
        print(f"{anni} :")
        while countdown != 0:
            if (anni-countdown) not in dizionario_anno:
                check = 0
                break
            countdown = countdown - 1
            media = sum(dizionario_anno[anni-countdown])/len(dizionario_anno[anni-countdown])
            somma = somma + media
            print(f"MEDIA: {media}")
            print(f"SOMMA: {somma}")
        
        if check == 1:
            media = (sum(dizionario_anno[anni])/len(dizionario_anno[anni])) - somma/N
            dizionario_media.update({anni : media})
    print(f"D_MEDIA: {dizionario_media}")
    return(dizionario_media)

        
docs = CSVTimeSeriesFile("data_esercitazione2.csv")
lista = docs.get_data()
compute_variations(lista, 1949, 1952)
compute_moving_average(lista, 1949, 1952, 2)
                