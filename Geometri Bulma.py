def geometri(sekil):
    if (len(sekil) == 3):
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a==b) and (a==c) and (b==c):
                print ("Eşkenar üçgendir.")

            elif (a==b) or (a==c) or (b==c):
                print ("İkizkenar üçgendir.")

            else :
                print ("Çeşitkenar üçgendir.")

        else :
            print ("Üçgen Belirtmiyor.")

                

    elif (len(sekil) == 4):
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a==b) and (a==c) and (a==d):
            print ("Şekil Karedir.")

        elif (a==c) and (b==d):
            print ("Dikdörtgen")

        else :
            print ("Dörtgen")


    else:
        print ("Herhangi bir sekil değil.")

while (True):
    eleman_sayisi = int(input ("Eleman sayısı giriniz: "))

    if (eleman_sayisi == 3):
       a = int(input ("a kenarını giriniz: "))
       b = int(input ("b kenarını giriniz: "))
       c = int(input ("c kenarını giriniz: "))

       geometri([a,b,c])

    elif (eleman_sayisi == 4):
       a = int(input ("a kenarını giriniz: "))
       b = int(input ("b kenarını giriniz: "))
       c = int(input ("c kenarını giriniz: "))
       d = int(input ("d kenarını giriniz: "))

       geometri([a,b,c,d])

    else :
        print ("Lütfen tekrar giriniz.")
    


