

def sort_no_dup(words):
    settato = set(words.split())
    ordinato = sorted(settato)
    print(ordinato)
    return(ordinato)

    #return sorted(set(words))

words = input('inserire lista parole separate da uno spazio:')
sort_no_dup(words)