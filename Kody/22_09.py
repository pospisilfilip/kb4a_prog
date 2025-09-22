def delitele(a):
    i = 1
    for i in range(i, a+1):
        if a % i == 0:
            print(i)

delitele(12)


def pyramida(vyska, znak):
    for i in range (1, vyska):
        print (znak) * i  

pyramida(10, "s")