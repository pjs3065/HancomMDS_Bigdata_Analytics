def add_num1(a,b):
    print("{} + {} = {}".format(int(a),int(b),int(a)+int(b)))
    return int(a)+int(b)

def add_num2(num_list):
    sum = 0
    for i in num_list:
        sum+=i
    return sum

print(add_num1(a = input(), b= input())) # 1번

num_list = list()

for i in range(0,4):  # 2번
    num_list.append(int(input()))
print(add_num2(num_list))
        
