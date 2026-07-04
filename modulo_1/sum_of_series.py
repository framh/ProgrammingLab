

def sum_of_series(num):
    sum_ = 0
    created_num= 0
    for i in range(0,4):
        created_num = created_num + (num * pow(10,i))
        sum_ = created_num + sum_
    print(sum_)

def somma_serie(num):
    sum_ = int(num) + int(num+num) + int(num+num+num) + int(num+num+num+num)
    print(sum_)

sum_of_series(7)
somma_serie('7')