"""
Create a program that calculates the sum of the digits
of a given integer using a while loop.
"""
num=int(input("Enter a number: "))

sum=0
while num>0:
    digit=num%10

    sum+=digit
    num//=10
print(sum)

