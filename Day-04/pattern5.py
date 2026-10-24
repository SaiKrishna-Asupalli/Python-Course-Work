r=7
for i in range(1,r+1):
    for s in range(r-i):
        print(" ",end=" ")
   
    for j in range(i):
        print("*",end="")
    for k in range(r-j):
        print(" ",end=" ")    

    print()