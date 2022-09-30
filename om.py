from turtle import left


print("SWAG Budet Program")
print(" This program will calculate how many SWAG Items may be purchased for a company from the money budgeted")
user_item=input(" Enter a Description of the SWAG item: ")
tax_amount=float(input("Enter the purchase price of each SWAG Item before tax: $"))
user_budget=int(input("Enter the total amount of money budgeted: $"))
amount_tax=tax_amount+(0.13*tax_amount)
number_item, left_money=divmod(user_budget,amount_tax)
print(f" With the total funds budgeted of ${user_budget} the company can buy {number_item} {user_item} at ${amount_tax} each (including 13% HST) for a total of ${user_budget-left_money}. There would still be ${round(left_money,2)} leftover.")



