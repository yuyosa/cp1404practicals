min_rate = 0.1
max_rate = 0.15
sales = float(input("your sales:"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * min_rate
    else:
        bonus = sales * max_rate
    print(f"{bonus: .2f}")
    sales = float(input("your sales:"))
print("Goodbye!")


