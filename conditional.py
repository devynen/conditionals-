"""
You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
Customers with a loyalty card get a 10% discount.
If the customer's order amount is above 20,000 NGN:
Loyalty card holders get an additional 5% discount.
Non-loyalty card holders get a free soft drink instead.
Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
Calculates the final discount or freebie for the customer.
Stores the result in a dictionary called order_summary.
Prints out a summary for the cashier.
"""

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

discount_pct = 0        
free_drink = False      


if customer["loyalty_card"]:
    discount_pct += 10 

if customer["order_amount"] > 20000:
    if customer["loyalty_card"]:
        discount_pct += 5   
    else:
        free_drink = True   


if customer["is_student"]:
    discount_pct += 5       


discount_value = customer["order_amount"] * discount_pct / 100
net_pay = customer["order_amount"] - discount_value

order_summary = {
    "customer": customer["name"],
    "original": customer["order_amount"],
    "discount_pct": discount_pct,
    "discount_value": discount_value,
    "net_pay": net_pay,
    "free_soft_drink": free_drink
}

# 5. Print for cashier
print(f"Name: {order_summary['customer']}")
print(f"Original: {order_summary['original']:,} NGN")
print(f"Discount: {order_summary['discount_pct']} % = {int(order_summary['discount_value']):,} NGN")
print(f"To pay: {int(order_summary['net_pay']):,} NGN")
print("Free soft drink:", "YES" if order_summary["free_soft_drink"] else "NO")


while i < 1000:
    print(i)

