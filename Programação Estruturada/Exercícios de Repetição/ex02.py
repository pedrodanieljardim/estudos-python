i : int = 0
sum : int = 0

while i <= 100:
    if i % 2 == 0:
        sum += i
    i +=1
else:
    print("A soma dos primeiros 50 números pares é {}".format(sum))