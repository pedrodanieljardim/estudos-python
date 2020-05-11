f = open("demofile.txt", "r")
print(f.read())
print('##############################')
f = open("demofile.txt", "r")
print(f.read(5))
print('##############################')
f = open("demofile.txt", "r")
for x in f:
  print(x)

f.close()