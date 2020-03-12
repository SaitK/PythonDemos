

print ("+ ------> Toplama")
print ("- ------> Çıkarma")
print ("* ------> Çarpma")
print ("/ ------> Bölme")

while (True):
    op = input("İşlemi seçiniz: ")

    if (op == "+"):
        op1 = input ("İlk sayıyı giriniz: ")
        op2 = input ("İkinci sayıyı giriniz: ")

        a = float (op1)
        b = float (op2)

        print (a+b)

    elif (op == "-"):
        op1 = input ("İlk sayıyı giriniz: ")
        op2 = input ("İkinci sayıyı giriniz: ")

        a = float (op1)
        b = float (op2)

        print (a-b)

    elif (op == "*"):
        op1 = input ("İlk sayıyı giriniz: ")
        op2 = input ("İkinci sayıyı giriniz: ")

        a = float (op1)
        b = float (op2)

        print (a*b)

    elif (op == "/"):
        op1 = input ("İlk sayıyı giriniz: ")
        op2 = input ("İkinci sayıyı giriniz: ")

        a = float (op1)
        b = float (op2)

        if (b == 0):
            print ("Bir sayı sıfıra bölünemez.")

        else :

            print (a/b)



        
