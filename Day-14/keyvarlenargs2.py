#normal parameter + **kwargs
def Userdetails(name,**details):
    print("name is: ",name)
    print("details are:",details)
Userdetails(name="sai",age=23,marks=90,color="red")