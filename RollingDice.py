import random
user score

computer_dice_1 = random.randrange(1,10)
computer_dice_2 = random.randrange(1,10)

print("Computer's choice")
print(computer_dice_1)
print(computer_dice_2)

user_dice_1 = input("Choose a number between 1-10 exclusively: ")
user_dice_2 = input("Choose a number between 1-10 exclusively: ")


def compareDice(dice1, dice2):
    # if dice1 > dice2
# Create a function that will compare a dice for the user to the computer and return:
#     a 2 points if the user has higher values
#     1 point if the user has the same vlaues
#     0 points if the user has lower values.
# Do this for each of the die pair (user, computer)
# Display points at the end. May loop this

"""
# NOTE:
1. Come up with a way to create a pairs of random numbers for the computer choice.
2. Accept user input and save to a variable.
3. Compare user input to the computer generated values.
4. Add an if else statement that displays a statement based on whether or not there is a match
"""
