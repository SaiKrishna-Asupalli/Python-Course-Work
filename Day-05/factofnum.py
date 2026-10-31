"""
Write a program to find all the factors
 of a given number using a while loop.
"""
num=int(input("Enter a number to find its factorials: "))

i=1
while i<num:
    if num%i==0:
        print(i)
    i+=1

print(i)
i+=1