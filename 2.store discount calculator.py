amount=int(input("Please enter the amount"))
if amount>50:
    discount_rate=20
    final_payment=amount*0.8
elif 20<amount<50:
    discount_rate=10
    final_payment=amount*0.9
else:
    discount_rate=0
    final_payment=amount
print("purchase amount:",final_payment)
