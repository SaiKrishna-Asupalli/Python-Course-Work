num=int(input("Enter a number: "))
if num<0:
    print("num is not a perfect square.")
else:
    root=num**0.5
    if root%1==0:
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")         