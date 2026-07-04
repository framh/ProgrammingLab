
def is_it_prime(x):
    counter=1

    for i in range(x):
        if x%(i+2) == 0 :
            if(counter >1):
                print('non è primo')
                return
            counter=counter+1
    print('è primo')

print('Di cosa vuoi sapere se è primo o no?')
x= int(input())
is_it_prime(x)
