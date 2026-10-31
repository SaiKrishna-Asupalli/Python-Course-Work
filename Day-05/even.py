"""
Write a while loop that prints all even numbers between 1 and 50.

"""
end=50
start=1
even=[]

while start<=end:
    if start%2==0:
        even.append(start)
    start+=1
print(even)

