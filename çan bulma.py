

vize1 = input("Vize 1 notunu girin: ")
vize2 = input("Vize 2 notunu girin: ")
final = input("final notunu girin: ")

a = float (vize1)
b = float (vize2)
c = float (final)

derece = a*0.3+b*0.3+c*0.4

print (derece)

if (derece >= 90):
    print ("Ders notunuz AA")

elif (derece >=75):
    print ("Ders notunuz BA")

elif (derece >=60) :
    print ("Ders notunuz BB")

elif (derece >=50):
    print ("Ders notunuz CB")

elif (derece >=40):
    print ("Ders notunuz CC")

elif (derece >=35):
    print ("Ders notunuz DC")

elif (derece >=25):
    print ("Ders notunuz DD")

elif (derece >=20):
    print ("Ders notunuz FD")

else :
    print ("Ders notunuz FF, Geçmiş olsun")

    

