
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
        print(f"LISTONE: {listone}")
        # settone = set(listone) Non si può fare perché listone contiene dati mutabili come le liste
        # print(f"SETTONE: {settone}")
        """
        per ovviare al problema di prima serve commutare tutte le liste in un elemento immutabile(hashable)
        come possono essere le tuple. Così ritorna un insieme di coppie di dati(data e valore) senza alcun 
        duplicato.
        
        """
        insieme = set(tuple(elemento) for elemento in listone) 
        print(f"INSIEME: {insieme}")
        no_dup_list = list(insieme)
        print(f"NO_DUP: {no_dup_list}")
        no_dup_listone = [list(elemento) for elemento in insieme]
        print(f"NO_LISTONE: {no_dup_listone}")
        return(listone)

docs = CSVTimeSeriesFile("precipitazioni2.csv")
lista = docs.get_data()
