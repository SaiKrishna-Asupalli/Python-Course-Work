hour=int(input("Enter current hour(0-24): "))
if hour>=5 and hour<12:
    print("Good morning")
elif hour>=12 and hour<16:
    print("Good afternoon")
elif hour>=16 and hour<20:
    print("Good evening")
elif hour>=0 and hour<5 or hour>=20 and hour<24:
    print("Good night")
else:
    print("Invalid hour input.")                