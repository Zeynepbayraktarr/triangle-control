a = input("birinci kenar:" )
b = input("İkinci Kenar:" )
hipotenüs = input("Hipotenüs:" )
a=int(a)
b=int(b)
hipotenüs=int(hipotenüs)


def ucgenmi(a,b,hipotenüs):
    if a**2+b**2 == hipotenüs**2:
        return "bu bir üçgendir !"
    else:
        return "bu bir üçgen değildir !!"

print(ucgenmi(a,b,hipotenüs))





