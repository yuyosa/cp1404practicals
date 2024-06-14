"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user enters a decimal or letter, a ValueError will occur.

2. When will a ZeroDivisionError occur?
When the user enters the value of the denominator, if the input is 0, a ZeroDivisionError will occur.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero! Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


