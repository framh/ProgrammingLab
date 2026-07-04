

class CSVTimeSeriesFile:

    def __init__(self, nome):
        if nome == "":
            raise ValueError(f'il nome non può essere vuoto.')
        
        if not isinstance(nome, str):
            raise TypeError('Errore: il nome inserito non è un tipo valido')
        try:
            with open(nome, 'r') as file:
                self.name = nome
        except FileNotFoundError as e:
            print(f'{e}')
        listone = []
        self.listone = listone
    
    def get_data(self):
        gate = 1

        with open(self.name, 'r') as file:
            contenuto = file.read()
            lista = contenuto.split()
            for i in lista:
                elementi = i.split(',')
                gate = 1
                for index in range(len(elementi)):
                    try: 
                        if index == 0:
                            #print('indice 0, data saltata')
                            continue
                        
                        float_version = float(elementi[index])
                        if float_version < 0:
                            gate = 0
                        #print('conversione float avvenuta')
                    except ValueError: 
                        gate = 0
                        print('riga ignorata, dato viziato.')
                
                if gate == 1:
                    self.listone.append(elementi)
            
            print(self.listone)
            return(self.listone)


def compute_avg(time_series, first_year, last_year):
    dizionario = {}
    counter = {}
    for elementi in time_series:
        no_barre = elementi[0].split('-')
        data = int(no_barre[0])
        # print(elementi)
        # print (data)
        if first_year <= data and last_year >= data:
            #print(f"data: {data}, first_year: {first_year}, confronto: {first_year <= data}")
            if data not in dizionario:

                    intero = float(elementi[1])
                    dizionario.update({data : intero})
                    counter.update({data : 1})
            
            else:
                dizionario[data] = dizionario[data] + float(elementi[1])
                counter[data] = counter[data] + 1
                print(dizionario)
    
    print(dizionario)
    # gate = 1
    # prev = 0
    # for elementi in time_series:
    #     no_barre = elementi[0].split('-')
    #     data = int(no_barre[0])
    #     print(data)
    #     if data != prev:
    #         gate = 1

    #     if gate == 1:
    #         prev = data
    #         gate = 0
    #         media = (dizionario[data]) / (counter[data])
    #         dizionario[data] = media
    for i in range(first_year, last_year+1): 
        try:
            media = (dizionario[i]) / (counter[i])
            dizionario[i] = media
        except KeyError as e:
            print(f'si è verificato un errore {e}')

    print(dizionario)
    return(dizionario)
            
#[['2020-01', '8.5'], ['2020-02', '9.2'], ['2020-04', '-3.1'], ['2021-01', '10.1'], ['2021-03', 
# '11.4'], ['2021-04', '9.8']]

temperature = CSVTimeSeriesFile('temperature.csv')
time_series = temperature.get_data()
compute_avg(time_series, 2020, 2021)
