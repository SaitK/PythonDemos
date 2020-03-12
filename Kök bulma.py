def kokbul(a,b,c):
    delta = (b*b-4*a*c)

    if (delta < 0):
        print ("Reel Kök Bulunmamaktadır.")
        return
    
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)

    return (x1,x2)


a = int(input ("Değişken a'yı giriniz: "))
b = int(input ("Değişken b'yi giriniz: "))
c = int(input ("Değişken c'yi giriniz: "))


print (kokbul (a,b,c))
