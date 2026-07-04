def transform_in_letters(lista):
    #lettere=[1, 'uno', 2, 'due', 3, 'tre', 4, 'quattro', 5, 'cinque', 6, 'sei', 7, 'sette', 8, 'otto', 9, 'nove']
    lettere=['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
    finale=[]
    #for ind, valore in enumerate(lettere):  
    for i in range(len(lista)):
        if(0<=lista[i] <=9):
            finale.append(lettere[lista[i]])

    print(finale)

lista=[]
for i in range(5):
    print('Aggiungi elemento alla lista:')
    x=int(input())
    lista.append(x)
transform_in_letters(lista)



