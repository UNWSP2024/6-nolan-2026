# By Nolan Nelsen
# Written on 2/27/2026
# Random Dice

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    # Sum 2 numbers
    total = roll1 + roll2

    # return sum to calling function
    return total

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
total_sum = 0

for i in range(100):
    total_sum += randDice()

average = total_sum / 100

print("Average of the 100 rolls: ", format(average, '.2f'))
