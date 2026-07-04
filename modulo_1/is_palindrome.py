def is_palindrome(lista):
    invertita= lista[ : : -1]
    for i in lista:
        if(lista[i] != invertita[i]):
            print('Non è palindromo!')
            return(False)
    print('è palindromo')
    return(True)

lista=[]
for i in range(5):
    print('Aggiungi elemento alla lista:')
    x=int(input())
    lista.append(x)
is_palindrome(lista)
        