def calculate_discount(price, discount_percent):
  if discount_percent >= 0.2:
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price
  else:
    return price    

price= float(input("Enter the price of the product: "))

discount_percent= float(input("Enter the discount percentage: "))

final_price= calculate_discount(price, discount_percent)

print("The final price of the product is:", final_price)



