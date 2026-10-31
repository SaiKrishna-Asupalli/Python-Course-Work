"""Use a while loop to calculate the factorial of a given number."""
num=int(input("Enter a number to cal the fact: "))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(fact)
