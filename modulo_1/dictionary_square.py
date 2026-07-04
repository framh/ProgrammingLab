

def dic_square(n):
    new_dictionary = dict()
    for i in range(1,n+1):
        new_dictionary[i] = pow(i,2) #oppure new_dictionary.update({key: value})
        
    print(new_dictionary)
    return(new_dictionary)

n = int(input())
dic_square(n)
print(dic_square(n))