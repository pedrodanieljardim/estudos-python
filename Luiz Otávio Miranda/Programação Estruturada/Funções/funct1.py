def soma(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input())
b = int(input())

print("A+B = {}".format( soma(a, b)))
print("A-B = {}".format( subtrai(a, b) ) )
print("A*B = {}".format( multiplica(a, b) ) )
print("A/B = {}".format( divide(a,b) ) )


