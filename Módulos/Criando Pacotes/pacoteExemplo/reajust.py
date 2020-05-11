def reajustInflation(a,b):
    if b > 0:
        return a + (a*(b/100))

def reajustDeflation(a,b):
    if b < 0:
        b = b/100
        return a + (a*b)
