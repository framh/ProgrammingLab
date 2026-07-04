

class ExamException(Exception):
    pass 


class CSVTimeSeriesFile():

    def __init__(self, nome):
        if nome == "":
            raise ExamException('Il nome non può essere vuoto')
        
        if not isinstance(nome, str):
            raise ExamException('errore nel tipo di file')

        try:
            with open(nome, 'r') as file:
                self.name = nome
                listone = []
                self.listone = listone
        except FileNotFoundError as e:
            raise ExamException(f'{e}')
    
    def get_data(self):
       

        with open(self.name, 'r') as file:
            contenuto = file.read()
            righe = contenuto.split()
            #print(contenuto)
            for riga in righe:
                eventi = riga.split()

                for singolo in eventi:
                    separati = singolo.split(',')
                    #print(separati)
                    try:
                        if float(separati[1]) < 0:
                            continue
                        separati_float = float(separati[1])
                        self.listone.append(separati)
                    except ValueError as e:
                        print(f'{e} dato viziato o mancante')  
                
            #print('listone: ', self.listone)
            return(self.listone)

def compute_max(time_series, first_year, last_year):
    dizionario = {}

    time_series.sort()
    print(time_series)
    for eventi in time_series:
        #eventi = time_series[0]
        #print(eventi)
        data = eventi[0].split('-')
# no_barre = time_series[0].split('-')
        #print('data: ', data)
#for i in range(first_year, last_year):
        anno = data[0]
        anno_intero = int(anno)
        #print('anno: ', anno)
        if anno_intero in range(first_year, last_year+1):
            if anno not in dizionario:
                numerico = float(eventi[1])
                dizionario.update({anno : eventi})
            
            else:
                floatati = float(eventi[1])
                if numerico < floatati:
                    numerico = floatati
                    dizionario[anno] = eventi
                # if dizionario[anno] < floatati:
                #     dizionario[anno] = floatati
    print(dizionario)




precipitazioni = CSVTimeSeriesFile('precipitazioni.csv')
dati = precipitazioni.get_data()
compute_max(dati, 2019, 2020)

        