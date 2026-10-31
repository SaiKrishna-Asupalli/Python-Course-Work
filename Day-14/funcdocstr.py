"""
How would you write a function with a docstring in Python? Can you show an example?
"""
def add(a,b):
    """
    this function adds two numbers and returns their sum


    """
    return a+b

result=add(10,20)
print(result)

print(add.__doc__)