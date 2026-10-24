a,b=0,1
for _ in range(10):
    print(a, end=" ")
    a,b=b, a+b
print()    
a=[1,2,3,4]
b=[1,2,3,4,5]
comm=list(set(a)&set(b))
print(comm)
 