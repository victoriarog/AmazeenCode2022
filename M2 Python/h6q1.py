import random

values = []
count = 20
pairs = 0

for i in range(count):
    values.append(random.randint(1, 10))

for i in range(count-1):
    if values[i] == values[i + 1]:
        pairs += 1

print(values)
print(pairs)

