num=int(input("Enter a number to check it is prime or not: "))
if num<2:
    print("its not prime")
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("its not prime")
            break
    else:
            print("its prime number")
           