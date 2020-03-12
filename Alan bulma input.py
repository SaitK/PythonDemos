inp1 = input ("a sayısını girin:")
inp2 = input ("b sayısını girin:")
inp3 = input ("c sayısını girin:")

a = float(inp1)
b = float(inp2)
c = float(inp3)

u = (a+b+c)/2

Alan = (u*(u-a)*(u-b)*(u-c))**0.5

print ("Kenarları %s, %s ve %s olan üçgenin alanı %s'dir" % (a,b,c,Alan))
