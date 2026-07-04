

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, nome):
        if not isinstance(nome, str):
            raise ExamException("Tipo di file errato")
        
        try:
            with open(nome, 'r') as file:
                self.name = nome
        
        except FileNotFoundError:
            raise ExamException("il file non è stato trovato o non esiste")
        listone = []
        self.listone = listone
    
    def get_data(self):
        with open(self.name, 'r') as file:
            righe = file.readlines()

            for riga in righe[1:]:
                eventi = riga.strip().split(",")
                try:
                    floatante = float(eventi[1])
                    if floatante < 0:
                        continue
                    self.listone.append(eventi)
                except ValueError:
                    print("dato viziato o mancante")
            print(self.listone)
            return(self.listone)


def compute_variation(time_series, first_year, last_year):
  
    if not (isinstance(first_year, int) or not isinstance(last_year, int)):
        raise ExamException("Il tipo degli anni non è un intero")
    
    if not (isinstance(time_series, list)):
        raise ExamException("Controllare il tipo della serie")
    
    if first_year > last_year:
        raise ExamException("Il primo anno non può essere più grande dell'ultimo")
   
    dizionario = {}

    registro_anni = {}
    for eventi in time_series:
        #print(eventi)
        data = eventi[0].split("-")
        #print(data)
        anno = data[0]
        print("anno: ", anno)
        valore_float = float(eventi[1])

        try: 
            anno_intero = int(anno)
        except ValueError:
            print("impossibile trasformare questo anno")
            continue
            #raise ExamException('impossibile trasformare questo anno')
        
        if anno_intero not in registro_anni:
            registro_anni.update({anno_intero : [valore_float]})
        
        else:
            #print("evento 1: ", eventi[1])
            registro_anni[anno_intero].append(valore_float)
    print("registro anni: ", registro_anni)
    
    if (first_year not in registro_anni or last_year not in registro_anni):
        raise ExamException("L'anno inserito non è presente nei registri.")
        
    for anno in registro_anni:
        if anno in range(first_year, last_year):
             chiave = str(anno) + "-" + str(anno + 1)

             media_anno = sum(registro_anni[anno])/ len(registro_anni[anno])
             media_succ = sum(registro_anni[anno+1])/ len(registro_anni[anno+1])
             differenza = media_succ - media_anno

             dizionario.update({chiave : differenza})
    print("dizionario: ", dizionario)
             


        


documento = CSVTimeSeriesFile('temperature2.csv')
lista = documento.get_data()
compute_variation(lista, 1900, 1903)