#variable length args
def itembillcal(*items):
    print(f"items are: {items}")
    print(f"total is: {sum(items)}")
itembillcal(100,200,300)
def itembillcal2(a,b,*items):
    print(f"a and b is: {a} and {b}")
    print(f"items are: {items}")
    print(f"total is: {sum(items)}")
itembillcal2(100,200,300,400)
