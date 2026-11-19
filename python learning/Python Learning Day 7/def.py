def discount(price, discount_percentage):
    final_price = price - (price*discount_percentage/100)
    return final_price


laptop_price = discount(80000, 10)
print("After discount price is: ", laptop_price)

with_tax = laptop_price + 2000
print("With GST:", with_tax)


def welcome_user(name, role="Customer"):
    return f"Welcome {name}! Your Role: {role}"


print(welcome_user("Ali", "Admin"))
print(welcome_user("Bilala"))


def bill(amount):
    tax = amount*0.15
    total = amount + tax
    return tax, total

tax, total = bill(1000)

print("Tax: ", tax, "| Total: ", bill)
