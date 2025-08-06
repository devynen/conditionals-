user_amount = float(input("Enter an amount to withdraw: "))
balance = 10000.0
new_balance= balance - user_amount

if user_amount <= balance:
    print("You can withdraw")
    
    if user_amount % 1000 == 0 and user_amount >0:
    print(f"Here is your cash and your balance is", new_balance)
    elif user_amount > balance:
    print("out of range")
    else:
        print("Invalid amount: must be in multiples of 1000")
else:
    print("Insufficient funds")

