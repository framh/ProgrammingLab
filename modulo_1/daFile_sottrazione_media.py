
class ExamException(Exception):
    pass 

def file_to_list(docs):
    list_of_lists = []
    #print(type(list_of_lists))
    with open(docs, 'r') as file:
        contenuto = file.read() 
        """ 
        righe = file.readlines() #praticamente legge già le singole righe del file
        for riga in righe[1:]:  # salta la prima riga
        """
        lista = contenuto.split()
        #print("lista: ", lista)
        for dati in lista:
            intern_list = dati.split(",")
            #print(intern_list)
            try:
                check = float(intern_list[1])
                if check > 0:
                   list_of_lists.append(intern_list)
            except ValueError as e:
                print("dato viziato o mancante")
        #print(list_of_lists)
        return(list_of_lists)
            

def compute_variation(time_series, first_year, last_year):
    if first_year > last_year:
        raise  ExamException("Valore del primo anno non può essere maggiore dell'ultimo")
    
    if not (isinstance(first_year, int) or isinstance(last_year, int)):
        raise ExamException("controlla la tipologia degli anni inseriti")
    
    if not isinstance(time_series, list):
        raise ExamException("La serie di dati non è del tipo lista")
    dizionario = {}

    registro_anni = {}
    time_series.sort()
    somma = 0

    for eventi in time_series:
        data = eventi[0].split("-")
        anno = data[0]
        try:
            anno_intero = int(anno)
            valore_intero = int(eventi[1])
            if anno_intero > last_year or anno_intero < first_year:
                print('Anno non utile per richiesta') #rimuovere una volta implementato
                continue

        except ValueError:
            print('Questo anno non è convertibile')
            continue
        
        if anno not in registro_anni:
            registro_anni.update({anno : [valore_intero]})
        
        else:
            registro_anni[anno].append(valore_intero)
    #print(registro_anni)

    for anno in registro_anni:
        anno_intero = int(anno)
        if anno_intero in range(first_year, last_year):
            chiave = anno+ "-" + str(int(anno) + 1)
            media_anno = sum(registro_anni[anno]) /len(registro_anni[anno])
            media_succ = sum(registro_anni[str(anno_intero+1)]) / len(registro_anni[str(anno_intero+1)])
            differenza = media_succ - media_anno
            #print(media_anno)
            #print(media_succ)

            dizionario.update({chiave : differenza})
    print(dizionario)


compute_variation(file_to_list("vendite.csv"), 2018, 2019)
compute_variation(file_to_list("vendite.csv"), 2018, 2020)
#file_to_list("vendite.csv")
