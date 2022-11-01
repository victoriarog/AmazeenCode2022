import random

numbers = int(input("how many numbers? "))
rows = int(input("how many rows? "))

for j in range(rows):
    for i in range (5):
        print(random.randint(0,10), end=' ')
    print()
