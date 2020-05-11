f = open('test.txt','w+')

f.write(input())
f.write('\n')
f.write(input())
f.write('\n')
f.write(input())
f.write('\n')
f.write(input())
f.write('\n')

f.seek(0,0)
print('Lendo linhas:')
print(f.read())

