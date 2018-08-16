def fibo(n):

    f = list()
    
    f.append(1)
    f.append(1)

    for i in range(2,n+1):
        f.append(f[i-1] +f[i-2])

    print("토끼의 수는 {}".format(f[n]))
        
fibo(int(input("개월 수 입력해라\n")))

