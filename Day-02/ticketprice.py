age=int(input("Enter age: "))
height=int(input("Enter height in feet: "))


if age<12:
    if height<4:
        print("Ticket price is $10.")
    else:
        print("Ticket price is $15.")
else:
    if height<4:
        print("Ticket price is $15.")
    else:
        print("Ticket price is $20")                             