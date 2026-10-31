  
num=int(input("Enter a number: "))
if num<0:
    print("its not a perfect cube.")
else:
    root=round(num**(1/3))
    if root**3==num:
        print(f"{num} is a perfect cube.")
    else:
        print(f"{num} is not a perfect cube.")        