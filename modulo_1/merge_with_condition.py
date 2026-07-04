

def merge_with_condition(lista1, lista2):
    
    # finale = [i for i in lista1 if i % 2 != 0]

    # for e in lista2:
    #     if e %2 == 0:
    #         finale.append(e)
    
    # ordinata = sorted(finale)
    # print(ordinata)
    lista3 = lista1 + lista2
    #print(lista3)
    finale = [i for i in lista3 if (i % 2 != 0 and i in lista1) or (i %2 ==0 and i in lista2) ]
    ordinata = sorted(finale)
    print(ordinata)



list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
merge_with_condition(list1, list2)