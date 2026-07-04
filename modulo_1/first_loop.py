

def first_loop(num):
    num = int(num)

    for i in range(1,num+1):

        for e in range(0,i):

            print(i, end ="")
        print('')

num = int(input('inserisci il numero che vuoi come MAX: '))
first_loop(num)