numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])# 3
print(numbers[-1])# 2
print(numbers[3])# 1
print(numbers[:-1])# I dont know
print(numbers[3:4])# 1
print(5 in numbers)# True
print(7 in numbers)# False
print("3" in numbers)# True
print(numbers + [6, 5, 3])# [3, 1, 4, 1, 5, 9, 2] [6, 5, 3]


# 1
numbers[0] = "ten"
print(numbers)
# 2
numbers[-1] = 1
print(numbers)
# 3
print(numbers[2:])
# 4
print(9 in numbers)
