setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6}
print('setA: {}'.format(setA))
print('setB: {}'.format(setB))
setC = setA.union(setB)
print("setC = setA u setB: {}".format(setC))
setD = setA.intersection(setB)
print("setC = setA ∩ setB: {}".format(setD))
setE = setB - setA
print('setE = setA - setB : {}'.format(setE))