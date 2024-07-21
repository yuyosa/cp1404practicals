"""
Pseudocode:
TOTAL_PRICE = 0
Get num of items

when num of items <= 0
    error
    Get num of items

for i in range(num of items):
    Get price
    TOTAL_PRICE += price

if TOTAL_PRICE > 100:
TOTAL_PRICE *= 0.9

print result

"""



TOTAL_PRICE = 0
num_items = int(input("number of items："))

while num_items <= 0:
    print("Invalid number of items!")
    num_items = int(input("number of items: "))


for i in range(num_items):
    price = float(input("items price："))
    TOTAL_PRICE += price

if TOTAL_PRICE > 100:
    TOTAL_PRICE *= 0.9

print(f"You have {num_items} items,Total price {TOTAL_PRICE:.2f} $")
