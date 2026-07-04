

def reverse_loop(num):

    for e in range(0,num+1):

        for i in range(0,num+1):
            print('*', end='')

        print()
        num-=1
    # Loop from 5 down to 1
    # for i in range(5, 0, -1):
    #     for j in range(0, i):
    #         print("*", end=" ")
    #     print("\n")
num = int(input('Numero MAX di dati: '))    
reverse_loop(num)