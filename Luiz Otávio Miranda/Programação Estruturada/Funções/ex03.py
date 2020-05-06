def calculaPorcento(a, b):
    a += (a * (1 / b))
    return a


a = int(input())
b = int(input())

print("{} + {}% = {}".format(a,b,calculaPorcento(a,b)))