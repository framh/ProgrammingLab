class fileCSV ():
    
    def __init__(self, nome):
        self.name=nome
    
    def get_data(self):
        """
        Il metodo si occupa di leggere un file CSV e di creare una lista di liste in cui sono 
        rappresentate tutte le righe del file, separando la data dal valore. La funzione ritorna
        tale lista di liste
        """
        file = open('shampoo_sales.csv', 'r')
        lista_finale=[]
        for line in file:   #in questo for creaiamo le liste checomporranno la lista di ritorno.
            # con lo strip rimuoviamo i caratteri di default "\n" inutile ai fini del controllo dati
            # con lo split invece ci occupiamo di dividere data dal dato.
            
            lista_interna = line.strip().split(',')
            lista_finale.append(lista_interna)
            #print(line)
        
        for indx in lista_finale: #questo for è inutile al fine della richiesta, ma è un controllo. 
            #                      Se mai implementata, rimuovere questo blocco
            print(indx)

        file.close()
        return(lista_finale)


vendite_shampoo = fileCSV('shampoo_sales.csv')
fileCSV.get_data(vendite_shampoo)