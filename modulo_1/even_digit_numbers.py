

def even_digit_numbers(start , end):
    
    lista_even = []
   
    for i in range(start , end+1):
        gate = 1
        esp = 1
        e = i
        while e != 0:
            #print ('1')
            resto = int(i%pow(10,esp))
            print (resto)
            e = int(e/pow(10,esp))
            print (i)
            if ((resto % 2) != 0):
                gate = 0
                #print ('2')
                break
           
        
        if gate == 1:
            lista_even.append(i)
    
    
    tupla = tuple(lista_even)
    print(tupla)
    return tupla
    #return ','.join([str(num) for num in range(start, end + 1) if all(int(digit) % 2 == 0 for digit in str(num))])

even_digit_numbers(1200,2010)
