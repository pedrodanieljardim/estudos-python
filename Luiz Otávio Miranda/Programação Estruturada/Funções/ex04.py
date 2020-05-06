def divide(a):
    if a % 2 == 0:
        return "fizz"
    elif a % 5 == 0 and a % 3 != 0:
        return "buzz"
    elif a % 5 == 0 and a % 3 == 0:
        return "FizzBuzz"
    else:
        return a


a = int(input())
print("{} = {}".format(a, divide(a)))
