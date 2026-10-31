num=int(input("Enter a number to get its multiples: "))
start=int(input("Enter the starting number: "))
end=int(input("Enter the end number: "))
multiple=[]
for i in range(start,end+1):
    if i%num==0:
        multiple.append(i)
print(multiple)
