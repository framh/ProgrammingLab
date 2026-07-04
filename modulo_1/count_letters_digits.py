

def conunt_letters_digits(stringa):
    numeri = [1,2,3,4,5,6,7,8,9,0] #range(0,10)
    counter_tot = 0
    counter = 0
    # for carattere in stringa:
    #     counter_tot+=1
    counter_tot = len(stringa)
    filtrati = [carattere for carattere in stringa if carattere.isdecimal()]
    
    counter = len(filtrati)
    
    print(f'i caratteri totali sono: {counter_tot} \n di cui numeri: {counter} \n e lettere: {counter_tot - counter}' )

stringa = 'Il 20/3/2005 successe che una bomba cadde in mare e rimbalzò fino al cielo. La forza di Archimede aveva fatto si che la bomba raggiungesse il cielo ed oltre 24 gabbiani morirono. I pesci festeggiarono con 0 perdite.'
conunt_letters_digits(stringa)