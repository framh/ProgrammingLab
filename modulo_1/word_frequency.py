

def word_frequency(stringa):
    word = input('che parola stai cercando nella stringa?')
    counter = 0
    minuscola = stringa.lower()
    parolina = word.lower()

    lista = minuscola.split()

    for i in lista:     #count = str_x.count("Emma") funzione che conta le ricorrenze
        if i == parolina:
            counter+=1
    
    print(f'la parola {word}, appare precisamente {counter} volte.')
    return(counter)

stringa = 'Emma is good developer. Emma is a writer'
word_frequency(stringa)
