

print('Di cosa vuoi pari o dispari?')
x= int(input())
def is_it_prime(x):
    counter=1

    for i in range(x):
        if x%(i+2) == 0 :
            if(counter >1):
                print('non è primo')
                return
            counter=counter+1
    print('è primo')
        


