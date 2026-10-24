amount=float(input("Enter total purchase amount: "))
if amount>=500:
   discount=amount*(20/100)
   print(f"discount is {discount}")
   price=amount-discount
   print(f"Final price after discount: {price}")
elif amount>=300:
   discount=amount*(10/100)
   print(f"discount is {discount}")
   price=amount-discount
   print(f"Final price after discount: {price}")
elif amount>=100:
   discount=amount*(5/100)
   print(f"discount is {discount}")
   price=amount-discount
   print(f"Final price after discount: {price}")
else:
   discount=amount*0
   print(f"no discount below 100 purchase")
   price=amount-discount
   print(f"Final price: {price}")
   