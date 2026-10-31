#Generate a pattern of numbers using nested for loops ?
num=int(input("enter a num: "))
pat=0
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()




