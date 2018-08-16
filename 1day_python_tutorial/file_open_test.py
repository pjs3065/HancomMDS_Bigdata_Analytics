f = open('test.txt','w')
f.write('나는 천재다')
f.close()

f = open('test.txt','r')
data = f.read()
f.close()
print(data)

with open('test.txt','r') as f:
    print(f.read())
