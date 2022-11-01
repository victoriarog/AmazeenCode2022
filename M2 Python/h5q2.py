import random

currentValue = 0

inputComp = random.randint(1, 5)

playersTurn = True #to track turn

print("Current value is: ", currentValue)

while True: 
    userVal = int(input("Input a number between 0 & 5: "))
    currentValue += userVal 
    print("Current value is: ", currentValue)
    print("Computer plays with: ", inputComp)
    currentValue += inputComp
    print("Current value is: ", currentValue)

