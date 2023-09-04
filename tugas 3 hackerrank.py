bilangan1=int(input())
bilangan2=int(input())
bilangan3=int(input())

if (bilangan1 > bilangan2 > bilangan3) or (bilangan3 > bilangan2 > bilangan1):
    bilangan_kedua_terbesar=bilangan2
elif (bilangan2 > bilangan1 > bilangan3) or (bilangan3 > bilangan1 > bilangan2):
    bilangan_kedua_terbesar=bilangan1
else:
    bilangan_kedua_terbesar=bilangan3
    
print(bilangan_kedua_terbesar)


