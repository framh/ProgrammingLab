

def division(a,b):
    try:
        print(a/b)
        return(a/b)
    except TypeError:
        print('controlla che sia un intero')
    except ZeroDivisionError:
        print('NON puoi dividere per 0')

division(4,2)
division(4,0)
division(4,'2')
