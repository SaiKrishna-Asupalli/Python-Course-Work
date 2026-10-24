num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
user=input("Enter operation: ")
if user=="+":
    sum=num1+num2+num3
    print(sum)
elif user=="*":
    mul=num1*num2*num3
    print(mul)
elif user=="/":
    div=num1/num2/num3
    print(div)     
else:
    print("Enter valid operation type")       
