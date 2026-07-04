print('Scegli una parola! Una qualsiasi:')
parola=input()
print('Ora scegli una lettera!')
x= input()
y=0
counter=0
for y in parola:
    if y==x:
        counter=counter+1
print("la tua lettera compare: ", counter, "volte")
