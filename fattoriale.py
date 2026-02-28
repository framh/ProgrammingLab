def fatto(prod, numero):
    prod=prod*numero
    return prod

print('di che numero vuoi il fattoriale?')
x=int(input())
prod=1
for i in range(1,x+1, 1):
    prod=fatto(prod,i)

print('il fattoriale è:', prod)