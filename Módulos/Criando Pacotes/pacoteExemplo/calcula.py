
def sum (a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b == 0:
        raise ValueError('N2 não pode ser 0!')
    else:
        return a/b

def multiply(a,b):
    return a*b

def compareLarger(a, b):
    if a > b:
        return a
    if a < b:
        return b