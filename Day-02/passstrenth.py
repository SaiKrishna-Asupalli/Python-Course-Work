password=input("Enter a password to check: ")
length=len(password)

if length>=12:
    print("Password strength: Strong")
elif length>=8:
    print("Password strength: Medium")
else:
    print("Password strength: Weak (Must be at least 8 characters)")        