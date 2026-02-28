def how_many_vocals(parola):
    vocali=['a','e','i','o','u']
    counter=0
    for i in parola:
        if i in vocali:
            counter=counter+1
    print('il numero di vocali è: ', counter)

print('di che parola vuoi sapere il numero di vocali?')
parola=input()
how_many_vocals(parola)
            