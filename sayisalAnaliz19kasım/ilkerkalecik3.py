import math

def fonksiyon(x):
    return 4 * 1 / math.e ** (0.5 * x) - x

def turevli(x):
    return -2 * 1 / math.e ** (0.5 * x) - 1

x0 = 2
iterasyon = 4
i = 0

while i < iterasyon:
    
    
    x1 = x0 - fonksiyon(x0) / turevli(x0)
    
    print("{}. İterasyon :".format(i + 1))
    
    print("x1:", format(x1))
    
    
    print("f(x1):", format(fonksiyon(x1)))


    x0 = x1
    i += 1



