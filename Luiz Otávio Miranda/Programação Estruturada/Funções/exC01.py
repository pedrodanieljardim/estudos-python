a = 10

def funct1(a):
    print(a)
    a *= 10
    print(a)

def funct2(a):
    print(a)
    return a * 10

funct1(funct2(a))