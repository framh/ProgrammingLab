

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, nome):
        
        if not isinstance(nome, str):
            raise ExamException("Controlla il tipo di nome inserito")
        if nome == "":
            raise ExamException("Il nome del file non può essere vuoto")
        
        try:
            with open(nome, 'r') as file:
                self.name = nome
        except:
            raise ExamException("Impossibile aprire il file")

        listone = []
        self.listone = listone
    
    def get_data(self):
        with open(self.name, 'r') as file:
            righe = file.readlines()
            
            for riga in righe[1:]:
                eventi = riga.strip().split(',')
                #print("eventi: ", eventi)

                try:
                    check = float(eventi[1])
                    if check < 0:
                        continue
                    self.listone.append(eventi)
                except:
                    print("dato mancante o viziato")
                    continue
            print(self.listone)
            return(self.listone)


def compute_variations(time_series, first_year, last_year, N):
    if not isinstance(time_series, list):
        raise ExamException("controllare tipo della serie")
    
    if not (isinstance(first_year, int) or isinstance(last_year, int)):
        raise ExamException("controllare tipo degli anni")
    
    if not isinstance(N, int):
        raise ExamException("Accettati solo numeri interi per gli anni precedenti")

    if N < 0:
        raise ExamException("Inserire un valore di N maggiore di 0")

    dizionario = {}

    registro_anni = {}

    for eventi in time_series:
        data = eventi[0].split('-')
        anno = data[0]
        anno_intero = int(anno)
        valore_float = float(eventi[1])

        if anno_intero not in registro_anni:
            registro_anni.update({anno_intero : [valore_float]})
        
        else:
            registro_anni[anno_intero].append(valore_float)
    print("registro anni: ", registro_anni)

    
    for anno in registro_anni:
        if anno not in range(first_year, last_year+1):
            print(f"{anno} non appartiene al range")
            continue
        
        if (anno - N) not in registro_anni:
            print("mancano dati anni precedenti per il calcolo")
            continue

        
        somma_medie = 0
        chiave = str(anno - N) + "-" + str(anno)
        media_anno = sum(registro_anni[anno])/len(registro_anni[anno])
        countdown = N
        while countdown != 0:
            
            if (anno - countdown) not in registro_anni:
                print(f"manca almeno un annno nel'intervallo, l'intervallo {chiave} sarà saltato")
                break
            media_N = sum(registro_anni[anno - countdown])/len(registro_anni[anno - countdown])
            somma_medie = somma_medie + media_N
            countdown = countdown-1
            
            if countdown == 0:
                media_anno = media_anno - (somma_medie/N)
                dizionario.update({chiave : media_anno})
        
        
    print("DIZIONARIO: ", dizionario)


            
docs = CSVTimeSeriesFile('GlobalTemperatures.csv')
serie = docs.get_data()
compute_variations(serie, 1900, 1904, 3)