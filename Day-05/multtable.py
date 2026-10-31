"""
Generate a multiplication table for a given number using
 a while loop.

"""
num=int(input("enter a number for multiplication table: "))
i=1
while i<=10:
    print(f"{num}*{i}=",num*i)
    i+=1