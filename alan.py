kenar1 = input("Birinci kenarı giriniz:")
kenar2 = input("İkinci kenarı giriniz:")
kenar3 = input("üçüncü kenarı giriniz:")

a = float(kenar1)
b = float(kenar2)
c = float(kenar3)

u = (a+b+c)/2

alan = (u*(u-a)*(u-b)*(u-c))**(0.5)

print ("Kenarları %s, %s ve %s olan üçgenin alanı %s'dir" %(kenar1,kenar2,kenar3,alan))

