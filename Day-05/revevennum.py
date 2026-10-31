"""
Implement a program that reverses even
 numbers using a while loop
"""

num1=int(input("Enter the even numbers: "))
rev=0

while num1>0:
    digit=num1%10
    rev=rev*10+digit
    num1=num1//10
print("Reversed number: ",rev)









