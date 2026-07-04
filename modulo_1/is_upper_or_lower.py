

def isupper_or_islower(stringa):
    conteggio = {'maiuscole' : 0, 
    'minuscole' : 0}

    for carattere in stringa:
        if carattere.isalpha():
            
            if carattere.isupper():
                conteggio['maiuscole'] += 1
            else:
                conteggio['minuscole'] += 1
    
    print(conteggio)

stringa = 'Il 20/3/2005 successe che una bomba cadde in mare e rimbalzò fino al cielo. La forza di Archimede aveva fatto si che la bomba raggiungesse il cielo ed oltre 24 gabbiani morirono. I pesci festeggiarono con 0 perdite.'
isupper_or_islower(stringa)