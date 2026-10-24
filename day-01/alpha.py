letter=str(input("Enter a character: "))
if len(letter)==1:
  if letter.isalpha():

    if letter.isupper():
        print("The character is uppercase letter. ")
    else:
        print("The character is lowercase letter. ")
  else:
    print("The character is not a letter.")            
else:
   print("Please enter only single character,")