def list_to_dic(lista):
    new_dictionary = {}
    for i in range(len(lista)):
        new_dictionary[i]= lista[i]
    print(new_dictionary)
    return(new_dictionary)
 

lista=[]
for i in range(5):
    print('Aggiungi elemento alla lista:')
    x=input()
    lista.append(x)

list_to_dic(lista)
print(list_to_dic(lista))
