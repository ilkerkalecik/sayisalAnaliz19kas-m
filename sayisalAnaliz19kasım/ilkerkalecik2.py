def fonksiyon(x):
    return x**3+4*x**2-10

x1 = 1
x2 = 2
x0 = float
y0 = float
a = fonksiyon(x1)
b = fonksiyon(x2)

iterasyon = 4
i = 0

while i <iterasyon:
    
    
    if a * b < 0:
        x0 = (x1 + x2) / 2
        y0 = fonksiyon(x0)

        print("{}. İterasyon".format(i + 1))
        
        
        print("x0: " + str(x0))

        print("y0: " + str(y0))


        if y0 * a < 0:
            x2 = x0
            
        elif y0 * b < 0:
            x1 = x0

    i += 1


