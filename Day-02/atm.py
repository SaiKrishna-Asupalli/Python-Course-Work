sai=1000
shireesha=2000
user=input("Enter your user name: ")

if user=="sai":
    amount=sai
    print(f"your balance is: {amount}")
    withdraw=int(input("Enter the money you want to withdraw: "))
    amount=sai-withdraw
    print(f"your current balance after withdraw: {amount}")
elif user=="shireesha":
    amount=shireesha
    print(f"your balance is: {amount}")
    withdraw=int(input("Enter the money you want to withdraw: "))
    amount=shireesha-withdraw   
    print(f"your current balance after withdraw: {amount}") 
else:
    print("Enter valid user name.")    
