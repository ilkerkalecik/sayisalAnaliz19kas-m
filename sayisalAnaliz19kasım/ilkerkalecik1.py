def fonksiyon(x):
   return x**3-x**2-5

x1 = 2
x2 = 4
x0 = float
y0 = float
a = fonksiyon(x1)
b = fonksiyon(x2)

i = 0
iterasyon = 4

while i < iterasyon:
    if a * b < 0:
        
        
        x0 = (x1 + x2) / 2
        y0 = fonksiyon(x0)


        if y0 * a < 0:
            x2 = x0
            
            
        elif y0 * b < 0:
            x1 = x0


    print("x0: " + str(x0))
    print("y0: " + str(y0))
    print()

    i += 1


