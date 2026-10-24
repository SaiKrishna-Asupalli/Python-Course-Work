age=int(input("Enter your age: "))
income=int(input("Enter your income: "))

if age>=18:
    
    #print("you are eligible.")
    if income>=25000:
        print("You are eligible to credit card.")
    else:
        print("Not eligible for credit card.")
else:
    print("You are not eligible")            