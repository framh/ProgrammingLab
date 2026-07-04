import curses

from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

snake = [[15,13], [15,12], [15,11]] #creazione serpente
cibo = [5,35] #creiamo il cibo alla riga e colonna impostata, ma non lo visualizziamo ancora
direzione_allo_spawn = KEY_DOWN
punti = 0

curses.initscr() #inizializzazione schermo
finestra = curses.newwin(30, 60, 0, 0,) #crea una finestra 30x60 e come spawn della finestra x=0 e y=0
finestra.keypad(True) #possibilità di usare le freccette
finestra.border(0) #bordo esterno al campo da gioco(distanza tra l'area di gioco e il limite della finestra)
velocità = max(60, 150 - punti * 5)
finestra.timeout(velocità) #il serpente si muove nella direzione della freccia o resta "fermo" nella direzione puntata precedentemente

finestra.addch(cibo[0], cibo[1], 'O') #con questa funzione aggiungo O alla riga e colonna


while True: #impostiamo di runnare il gioco
    
    finestra.addstr(0, 14, 'Punteggio:' + str(punti) + '') #posizionamo al centro e che viene sempre 
    #mostrato il punteggio
    tasto = finestra.getch() #aggiorna lo schermo ad ogni frame e prende il tasto premuto
    if tasto != -1:
        direzione_allo_spawn = tasto #salviamo dentro il tasto premuto

    nuovatesta = copy(snake[0]) #così creiamo una copia della testa ad ogni refresh

    #per ogni direzione andiamo a creare una testa in una posizione differente
    # (non sposto la stessa testa, ma creo questa illusione creandone altre)
    if direzione_allo_spawn == KEY_DOWN:
        nuovatesta[0] += 1
    elif direzione_allo_spawn == KEY_UP:
        nuovatesta[0] -= 1
    elif direzione_allo_spawn == KEY_LEFT:
        nuovatesta[1] -= 1
    elif direzione_allo_spawn  == KEY_RIGHT:
        nuovatesta[1] += 1
    
    snake.insert(0, nuovatesta) #inserimento nuova testa
    if snake[0][0] == 0 or snake[0][0] == 29 or snake[0][1]  == 0 or snake[0][1] == 59:
       #se ci scantiamo contro i bordi della finestra
        break

    if snake[0] in snake[1:]:
        #se ci scantiamo contro il corpo
        break

    if snake[0] == cibo:
        #se prendiamo il cibo cosa succede?
        cibo = []
        punti +=1
        while cibo == []:
            #generiamo prossimo cibo
            cibo = [randint(1, 28), randint(1, 50)]
            if cibo in snake:
                cibo = []
            finestra.addch(cibo[0], cibo[1], 'O') #aggiunge prossimo cibo
    #se snake finisce su qualunque altra casella  
    else:
        ultimo_pezzo = snake.pop() #estraiamo l'ultimo pezzo del snake e metti ' '
        finestra.addch(ultimo_pezzo[0], ultimo_pezzo[1], ' ')
    finestra.addch(snake[0][0], snake[0][1], 'x') #come visualizziamo il serpente(una serie di x)

curses.endwin() #E' il GAME OVER
print(f'\n GAME OVER \n punteggio: {punti}')




