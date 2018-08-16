man_count = 0

for i in range(10001):
    i = str(i)
    for j in range(len(i)):
        if i[j] == '8':
            man_count += 1
print("1만까지 8의 등장 수는 {}".format(man_count))


print(str(list(range(10000))).count('8'))        
    
        
    
    
