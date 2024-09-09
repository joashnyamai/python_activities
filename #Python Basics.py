#Program to compute Discount
total_amount = float(input("Enter the amount purchased: "))
if total_amount > 1000:
    discount = 0.05 * total_amount
    price_after_discount = total_amount - discount
    print("The discount is", discount)
    print("The price after discount is", price_after_discount)
else:
    print("No discount")