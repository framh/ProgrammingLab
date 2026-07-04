def is_a_triangle(lato1, lato2, lato3):

    if(lato1 + lato2 > lato3 and abs(lato1 - lato2) < lato3 
        and lato1 + lato3 > lato2 and abs(lato1 - lato3) < lato2 
        and lato3 + lato2 > lato1 and abs(lato3 - lato2) < lato1):

        if lato1 != lato2 or lato1 != lato3 or lato2 != lato3: 
            if lato1 == lato2 or lato1 == lato3 or lato2 ==lato3:
                print('il triangolo esiste ed è isoscele!')
                return
            else:
                print('il triangolo esiste ed è scaleno!')
                return
        else:
            print('il triangolo esiste ed è equilatero!')
            return
    else:
        print('non esiste un triangolo con queste misure!')

print('dammi i 3 lati e ti dico se ci puoi costruire un triangolo ')
x=int(input())
y=int(input())
z=int(input())
is_a_triangle(x,y,z)