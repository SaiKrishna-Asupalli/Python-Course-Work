password=1234
pass1=int(input("Enter the password: "))

while password!=pass1:
    print("Incorrect password! Try again:")
    pass1=input("Enter the password:")
print("Correct password! Access granted.")