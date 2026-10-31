#Find and print the position (index) of an element in a list using a for loop ?
s=[1,2,3,4,5]
element=int(input("Enter the element to search: "))
for i in range(len(s)):
    if element==s[i]:
        print(f"{element} Element is found at the index: {i}")
        break
else:
        print("Enter not found ")


