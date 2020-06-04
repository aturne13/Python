import random

computer_dice_1 = random.randrange(1,10)
computer_dice_2 = random.randrange(1,10)

print("Computer's choice")
print(computer_dice_1)
print(computer_dice_2)

user_dice_1 = input("Choose a number between 1-10 exclusively: ")
user_dice_2 = input("Choose a number between 1-10 exclusively: ")

print("User's choice")
print(user_dice_1)
print(user_dice_2)


"""
# NOTE:
1. Come up with a way to create a pairs of random numbers for the computer choice.
2. Accept user input and save to a variable.
3. Compare user input to the computer generated values.
4. Add an if else statement that displays a statement based on whether or not there is a match
"""
