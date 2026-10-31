"""
Write a program using a while loop to generate
the first n terms of the Fibonacci sequence.
"""
n=int(input("Enter a num: "))
a=0
b=1
count=0
while count<n:
    c=a+b
    a=b
    b=c
    print(a,end=" ")
    count+=1



