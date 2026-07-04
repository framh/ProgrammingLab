

def sort_word(parole):
    lista = parole.split(',')
    ordinata = sorted(lista)
    print(ordinata)
    # return ','.join(sorted(parole.split(',')))

parole=input('inserire parole separate da una virgola:')
sort_word(parole)