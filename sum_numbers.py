def somma(sum, numero):
    sum=sum+numero
    return(sum)
    

sum=0
x=-1
while x!=0:
    print('che numeri vuoi sommare?')
    x=int(input())
    if x !=0:
        sum=somma(sum,x)

print('la somma è:', sum)