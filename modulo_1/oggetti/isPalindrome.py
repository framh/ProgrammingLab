

def isPalidrome(num):
    num = str(num)
    lista = [i for i in num]
    invertita = list(reversed(lista)) #invertita = lista[::-1]
    print(lista)
    print(invertita)

    if lista == invertita:
        print('è palindromo')
        return(1)
    print('non è palindromo')
    return(0)

isPalidrome(1241)