a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a<b and a<c:
    print(f"{a} is the smallest.")
elif b<a and b<c:
    print(f"{b} is the smallest.")
else:
    print(f"{c} is the smallest.")        