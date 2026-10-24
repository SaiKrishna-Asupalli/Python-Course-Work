grade=int(input("Enter your grade: "))
if grade<70:
    print("You failed")
    if grade>=60:
        print("Letter grade: D")
    else:
        print("Letter grade: F")
else:
    print("You passed")
    if grade>=90:
        print("Letter grade: A")
    elif grade>=80:
        print("Letter grade: B")
    elif grade>=70:
        print("Letter grade: C")                    
       