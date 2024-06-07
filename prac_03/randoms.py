# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
#A: An integer number is displayed
#I ran each line of code four times, with the smallest number being 7 and the largest being 20.


# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
#A: In this row of data generation, I found that the numbers only generate 3, 5, 7, 9
#The smallest number is 3 and the largest number is 9
#Impossible, because the code actually means to generate one of the four numbers 3, 5, 7, 9


# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
#A: A number with 16 decimal places is generated from 2.5-5.5
# The smallest number is 2.5226639455455473
# The largest number is 4.5139190399282825
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
random_number = random.randint(1, 100)
print(random_number)
