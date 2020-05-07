# declaração direta de um set (conjunto)
s1 = {1, 2, 3, 4, 5, 6}

print("Set s1: {}".format(s1))

s1.add(7)
s1.add(8)
s1.add(9)
s1.add(10)

print("Set s1: {}".format(s1))

print("=============================")
s2 = set()
print("Set s2: {}".format(s2))
s2.add(11)
s2.add(12)
s2.add(13)
s2.add(14)
s2.add(15)
print("Set s2: {}".format(s2))

print("=============================")
s3 = set()
print("Set s3: {}".format(s3))
s3.update(s1, s2)
print("Set s3: {}".format(s3))



