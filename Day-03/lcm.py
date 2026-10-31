#Calculate the LCM (Least Common Multiple) of two numbers using a for loop ?
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1==0 or num2==0:
    print("LCM IS 0")
else:
    for i in range(max(num1,num2),(num1*num2)+1):
        if i%num1==0 and i%num2==0:
            print("LCM =", i)
            break