print("""
    *
   ***
  *****
 *******
*********""")

for i in range(0,5):
    for k in range(0,4-i):
        print(" ",end='')

    
    for j in range(0,i*2+1):
        print("*",end='')
    print("\n",end='')        
