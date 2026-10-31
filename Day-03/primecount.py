start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))

count=0
for n in range(start,end+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            count+=1
print("Count of prime numbers: ",count)








