import random

values = [random.randint(1, 10) for i in range(20)]
values.sort()
print(values)

x = 4
l = 0 #ind 1st element
r = len(values) - 1 # ind last element
i = (r + l) // 2

while r >= l:
    i = (r + l) // 2

    if x > values[i]:
        print("x is on the right")
        l = i + 1
    elif x < values[i]:
        print("x is on the left")
        r = i - 1
    elif x == values[i]:
        print(str(x) + " is in the list, position " + str(i))
        break
    else: 
        print("x is not on the list")
        break
