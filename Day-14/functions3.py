name="sai"
def display():
    name="krishna"
    print("enclose:",name)
    def inner():
        name="reddy"
        print("inner:",name)
    inner()

display()
print("global:",name)
