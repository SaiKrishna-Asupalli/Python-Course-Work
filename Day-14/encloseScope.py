"""
How would you demonstrate enclosing scope in Python with an example?
"""
def outer():
    name="sai"
    def inner():
        name="krishna"
        print("enclose:",name)
    inner()
    print("inner : ",name)
outer()




