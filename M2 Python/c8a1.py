import random

values = []
count = 20

for i in range(count):
    values.append(random.randint(1, 10))    

for i in range(count):
    print(values[i], end=' ')
    if (i + 1) % 5 == 0 :
        print()